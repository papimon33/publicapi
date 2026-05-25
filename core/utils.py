import os
import re
import json
import asyncio
import inspect
from contextvars import ContextVar
from typing import List, Tuple, Any
from fastapi import HTTPException

# type=sql 요청 시 DB 실행을 건너뛰고 SQL을 캡처하기 위한 컨텍스트 변수.
# ContextVar에 mutable dict를 저장해 task 간 참조를 공유한다.
_sql_capture: ContextVar[dict | None] = ContextVar('_sql_capture', default=None)


def _xml_escape(value) -> str:
    return (str(value)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;"))


def transform_for_json(data: dict) -> dict:
    result = {}
    if 'header' in data:
        result['header'] = data['header']
    body = data.get('body')
    if body is not None:
        result['body'] = {
            'numOfRows': body.get('numOfRows'),
            'pageNo': body.get('pageNo'),
            'totalCount': body.get('totalCount'),
            'items': {'item': body.get('data', [])},
        }
    return result


def json_to_xml(data: dict) -> str:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<response>']

    header = data.get('header', {})
    lines.append('  <header>')
    lines.append(f'    <resultCode>{_xml_escape(header.get("resultCode", ""))}</resultCode>')
    lines.append(f'    <resultMessage>{_xml_escape(header.get("resultMessage", ""))}</resultMessage>')
    lines.append('  </header>')

    body = data.get('body')
    if body is not None:
        lines.append('  <body>')
        lines.append(f'    <numOfRows>{body.get("numOfRows", "")}</numOfRows>')
        lines.append(f'    <pageNo>{body.get("pageNo", "")}</pageNo>')
        lines.append(f'    <totalCount>{body.get("totalCount", "")}</totalCount>')
        lines.append('    <items>')
        for item in body.get('data', []):
            lines.append('      <item>')
            for key, value in item.items():
                v = '' if value is None else _xml_escape(value)
                lines.append(f'        <{key}>{v}</{key}>')
            lines.append('      </item>')
        lines.append('    </items>')
        lines.append('  </body>')

    lines.append('</response>')
    return '\n'.join(lines)

def validate_required(request, *fields: str):
    missing = [f for f in fields if getattr(request, f, None) is None]
    if missing:
        raise HTTPException(
            status_code=400,
            detail={
                "resultCode": "01",
                "resultMessage": f"필수 파라미터가 없습니다: {', '.join(missing)}",
            },
        )


def get_sql_query(method_name: str) -> str:
    frame = inspect.stack()[1]
    caller_file = frame.filename
    base_dir = os.path.dirname(os.path.dirname(caller_file))
    domain = os.path.splitext(os.path.basename(caller_file))[0]
    sql_path = os.path.join(base_dir, 'sql', domain, f'{method_name}.sql')
    with open(sql_path, 'r', encoding='utf-8') as f:
        return f.read()

def build_conditions(query: str, request: Any, mapping: List[tuple]) -> Tuple[str, list]:
    cond_sql = ""
    params = []
    for item in mapping:
        attrs = item[0] if isinstance(item[0], tuple) else (item[0],)
        sql_fragment = item[1]

        if not attrs:
            continue

        all_present = all(getattr(request, attr, None) is not None for attr in attrs)
        if all_present:
            cond_sql += " " + sql_fragment
            for attr in attrs:
                params.append(getattr(request, attr))

    order_match = re.search(r'\bORDER\s+BY\b', query, re.IGNORECASE)
    if order_match and cond_sql:
        query = query[:order_match.start()] + cond_sql + " " + query[order_match.start():]
    else:
        query += cond_sql

    return query, params

def wrap_pagenation_sql(original_sql: str, request: Any) -> Tuple[str, str]:
    if hasattr(request, 'pageNo') and hasattr(request, 'numOfRows'):
        page_no = request.pageNo
        num_of_rows = request.numOfRows
        start_row = (page_no - 1) * num_of_rows
        end_row = page_no * num_of_rows

        # COUNT 쿼리에서 최상위 ORDER BY 제거 (일부 DB에서 에러 발생 방지)
        sql_for_count = re.sub(
            r'\s+ORDER\s+BY\s+\S.*$', '',
            original_sql.strip(),
            flags=re.IGNORECASE | re.DOTALL
        )

        # Count SQL — 닫는 ) 를 별도 줄에 써야 SQL 내 -- 주석이 ) 를 삼키지 않음
        count_sql = f"SELECT COUNT(*) FROM (\n{sql_for_count}\n)"

        # Paginated SQL (Oracle / Tibero ROWNUM 방식)
        paginated_sql = f"""SELECT * FROM (
    SELECT A.*, ROWNUM AS RNUM FROM (
{original_sql}
    ) A WHERE ROWNUM <= {end_row}
) WHERE RNUM > {start_row}"""
        # 반환 순서: (count_sql, paginated_sql) — execute_query 파라미터 순서와 일치
        return count_sql, paginated_sql
    return "", original_sql

async def execute_query(conn, count_query: str, paginated_query: str, params: list) -> Tuple[int, list]:
    """
    공용 DB 쿼리 실행 헬퍼.
    count 쿼리와 paginated 쿼리를 순서대로 실행하고 (total_count, result) 를 반환합니다.
    각 execute() 호출에 DB_QUERY_TIMEOUT 을 적용합니다.
    _sql_capture 가 설정된 경우(type=sql 요청) DB를 실행하지 않고 SQL만 캡처하여 반환합니다.
    """
    capture = _sql_capture.get(None)
    if capture is not None:
        capture.update({
            'count_query': count_query,
            'paginated_query': paginated_query.strip(),
            'params': [str(p) if p is not None else 'NULL' for p in params],
        })
        return 0, []

    from db.connection import DB_QUERY_TIMEOUT  # 순환 import 방지를 위해 지연 import

    async with conn.cursor() as count_cursor:
        async with asyncio.timeout(DB_QUERY_TIMEOUT):
            await count_cursor.execute(count_query, params)
        count_row = await count_cursor.fetchone()
        total_count = count_row[0] if count_row else 0

    async with conn.cursor() as cursor:
        async with asyncio.timeout(DB_QUERY_TIMEOUT):
            await cursor.execute(paginated_query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]

    return total_count, result
