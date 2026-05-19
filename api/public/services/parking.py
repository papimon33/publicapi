import os
import aioodbc
from typing import List, Dict, Any, Tuple
from api.public.models.parking import *
from core.models import PaginationResponse, PaginationParams
from core.utils import build_conditions, get_sql_query, wrap_pagenation_sql, execute_query


async def fetch_valet_congestion(request: ValetCongestionRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[ValetCongestionResponse]:
    query = get_sql_query('get_valet_congestion')
    query, params = build_conditions(query, request, [])
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[ValetCongestionResponse](body={"data": [ValetCongestionResponse(**row) for row in result], "numOfRows": page.numOfRows, "pageNo": page.pageNo, "totalCount": total_count})

async def fetch_parking_congestion(request: ParkingCongestionRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[ParkingCongestionResponse]:
    query = get_sql_query('get_parking_congestion')
    query, params = build_conditions(query, request, [])
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
    query, params = build_conditions(query, request, [])
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[AirportParkingResponse](body={"data": [AirportParkingResponse(**row) for row in result], "numOfRows": page.numOfRows, "pageNo": page.pageNo, "totalCount": total_count})

async def fetch_parking_cell_gmp(request: ParkingCellGmpRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[ParkingCellGmpResponse]:
    query = get_sql_query('get_parking_cell_gmp')
    query, params = build_conditions(query, request, [])
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[ParkingCellGmpResponse](body={"data": [ParkingCellGmpResponse(**row) for row in result], "numOfRows": page.numOfRows, "pageNo": page.pageNo, "totalCount": total_count})
