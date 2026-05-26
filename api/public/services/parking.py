import os
import re
import aioodbc
from typing import List, Dict, Any, Tuple
from api.public.models.parking import *
from core.models import PaginationResponse, PaginationParams
from core.utils import build_conditions, get_sql_query, wrap_pagenation_sql, execute_query

_PARKING_CODE_MAP = {
    'GMP': 1, 'PUS': 2, 'CJU': 3, 'TAE': 4, 'KWJ': 5,
    'RSU': 6, 'USN': 7, 'KUV': 8, 'WJU': 9, 'CJJ': 10,
    'MWX': 11, 'HIN': 12, 'YNY': 13,
}

def _insert_before_order(query: str, cond: str) -> str:
    m = re.search(r'\bORDER\s+BY\b', query, re.IGNORECASE)
    if m:
        return query[:m.start()] + cond + ' ' + query[m.start():]
    return query + cond


async def fetch_valet_congestion_gmp_dom(request: ValetCongestionGmpDomRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[ValetCongestionGmpDomResponse]:
    query = get_sql_query('get_valet_congestion')
    query, params = build_conditions(query, request, [])
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[ValetCongestionGmpDomResponse](body={"data": [ValetCongestionGmpDomResponse(**row) for row in result], "numOfRows": page.numOfRows, "pageNo": page.pageNo, "totalCount": total_count})

async def fetch_parking_congestion(request: ParkingCongestionRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[ParkingCongestionResponse]:
    query = get_sql_query('get_parking_congestion')
    params = []
    if request.schAirportCode:
        code = _PARKING_CODE_MAP.get(str(request.schAirportCode).upper())
        if code:
            query = _insert_before_order(query, "AND A.PARKING_AIRPORT_CODE = ?")
            params.append(code)
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[ParkingCongestionResponse](body={"data": [ParkingCongestionResponse(**row) for row in result], "numOfRows": page.numOfRows, "pageNo": page.pageNo, "totalCount": total_count})

async def fetch_parking_fee(request: ParkingFeeRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[ParkingFeeResponse]:
    query = get_sql_query('get_parking_fee')
    query, params = build_conditions(query, request, [
        ('schAirportCode', "AND B.SITE_NAME2 = UPPER (?)"),
    ])
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[ParkingFeeResponse](body={"data": [ParkingFeeResponse(**row) for row in result], "numOfRows": page.numOfRows, "pageNo": page.pageNo, "totalCount": total_count})

async def fetch_airport_parking(request: AirportParkingRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[AirportParkingResponse]:
    query = get_sql_query('get_airport_parking')
    params = []
    if request.schAirportCode:
        code = _PARKING_CODE_MAP.get(str(request.schAirportCode).upper())
        if code:
            query = _insert_before_order(query, "AND A.PARKING_AIRPORT_CODE = ?")
            params.append(code)
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[AirportParkingResponse](body={"data": [AirportParkingResponse(**row) for row in result], "numOfRows": page.numOfRows, "pageNo": page.pageNo, "totalCount": total_count})

async def fetch_available_spaces_gmp_int_indoor(request: AvailableSpacesGmpIntIndoorRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[AvailableSpacesGmpIntIndoorResponse]:
    query = get_sql_query('get_parking_cell_gmp')
    query, params = build_conditions(query, request, [])
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[AvailableSpacesGmpIntIndoorResponse](body={"data": [AvailableSpacesGmpIntIndoorResponse(**row) for row in result], "numOfRows": page.numOfRows, "pageNo": page.pageNo, "totalCount": total_count})
