import os
import aioodbc
from typing import List, Dict, Any, Tuple
from api.public.models.noise import *
from core.models import PaginationResponse, PaginationParams
from core.utils import build_conditions, get_sql_query, wrap_pagenation_sql, execute_query


async def fetch_noise_stats(request: NoiseStatsRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[NoiseStatsResponse]:
    query = get_sql_query('get_noise_stats')
    base_params = [getattr(request, 'year', None)] * 13
    cond_query, params = build_conditions(request, [('airportCode', "AND T1.ARP_SE = ?")])
    query += cond_query
    params = base_params + params
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[NoiseStatsResponse](body={"data": [NoiseStatsResponse(**row) for row in result], "numOfRows": page.numOfRows, "pageNo": page.pageNo, "totalCount": total_count})

async def fetch_noise_affected_area(request: NoiseAffectedAreaRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[NoiseAffectedAreaResponse]:
    query = get_sql_query('get_noise_affected_area')
    base_params = [getattr(request, 'city1', None), getattr(request, 'city2', None), getattr(request, 'dong', None)] * 10
    cond_query, params = build_conditions(request, [
        ('city1', "AND T1.CTP_NM LIKE '%'||?||'%'"),
        ('city2', "AND T1.SIG_NM LIKE '%'||?||'%'"),
        ('dong', "AND T1.HEMD_NM LIKE '%'||?||'%'"),
        ('li', "AND T1.LI_NM LIKE '%'||?||'%'"),
        ('jibun', "AND TO_CHAR(DECODE(TO_CHAR(LNBR_SLNO), TO_CHAR('0'), TO_CHAR(LNBR_MNNM), CONCAT(TO_CHAR(LNBR_MNNM), CONCAT('-' , TO_CHAR(LNBR_SLNO))))) LIKE '%'||?||'%'"),
        ('street', "AND T1.RN LIKE '%'||?||'%'"),
        ('build', "AND T1.BULD_NM LIKE '%'||?||'%'"),
        ('buildno', "AND TO_CHAR(DECODE(TO_CHAR(BULD_SLNO), TO_CHAR('0'), TO_CHAR(BULD_MNNM), CONCAT(TO_CHAR(BULD_MNNM), CONCAT('-' , TO_CHAR(BULD_SLNO))))) LIKE '%'||?||'%'"),
        ('hosu', "AND T1.BULD_HOSU LIKE '%'||?||'%'"),
    ])
    query += cond_query
    params = base_params + params
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[NoiseAffectedAreaResponse](body={"data": [NoiseAffectedAreaResponse(**row) for row in result], "numOfRows": page.numOfRows, "pageNo": page.pageNo, "totalCount": total_count})

async def fetch_noise_realtime_gmp(request: NoiseRealtimeGmpRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[NoiseRealtimeGmpResponse]:
    query = get_sql_query('get_noise_realtime_gmp')
    cond_query, params = build_conditions(request, [])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[NoiseRealtimeGmpResponse](body={"data": [NoiseRealtimeGmpResponse(**row) for row in result], "numOfRows": page.numOfRows, "pageNo": page.pageNo, "totalCount": total_count})

async def fetch_noise_realtime_pus(request: NoiseRealtimePusRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[NoiseRealtimePusResponse]:
    query = get_sql_query('get_noise_realtime_pus')
    cond_query, params = build_conditions(request, [])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[NoiseRealtimePusResponse](body={"data": [NoiseRealtimePusResponse(**row) for row in result], "numOfRows": page.numOfRows, "pageNo": page.pageNo, "totalCount": total_count})
