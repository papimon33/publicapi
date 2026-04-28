import os
import aioodbc
from typing import List, Dict, Any, Tuple
from .models import *
from core.utils import build_conditions, get_sql_query

async def fetch_valet_congestion(request: ValetCongestionRequest, conn: aioodbc.Connection) -> List[ValetCongestionResponse]:
    query = get_sql_query('get_valet_congestion')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [ValetCongestionResponse(**row) for row in result]

async def fetch_parking_congestion(request: ParkingCongestionRequest, conn: aioodbc.Connection) -> List[ParkingCongestionResponse]:
    query = get_sql_query('get_parking_congestion')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [ParkingCongestionResponse(**row) for row in result]

async def fetch_parking_fee(request: ParkingFeeRequest, conn: aioodbc.Connection) -> List[ParkingFeeResponse]:
    query = get_sql_query('get_parking_fee')

    cond_query, params = build_conditions(request, [
        ('schAirportCode', "AND B.SITE_NAME2 = UPPER (?)"),
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [ParkingFeeResponse(**row) for row in result]

async def fetch_airport_parking(request: AirportParkingRequest, conn: aioodbc.Connection) -> List[AirportParkingResponse]:
    query = get_sql_query('get_airport_parking')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [AirportParkingResponse(**row) for row in result]

async def fetch_parking_cell_gmp(request: ParkingCellGmpRequest, conn: aioodbc.Connection) -> List[ParkingCellGmpResponse]:
    query = get_sql_query('get_parking_cell_gmp')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [ParkingCellGmpResponse(**row) for row in result]

