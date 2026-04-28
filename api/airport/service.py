import os
import aioodbc
from typing import List, Dict, Any, Tuple
from .models import *
from core.utils import build_conditions, get_sql_query

async def fetch_lease_contract(request: LeaseContractRequest, conn: aioodbc.Connection) -> List[LeaseContractResponse]:
    query = get_sql_query('get_lease_contract')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [LeaseContractResponse(**row) for row in result]

async def fetch_transport_stats(request: TransportStatsRequest, conn: aioodbc.Connection) -> List[TransportStatsResponse]:
    query = get_sql_query('get_transport_stats')

    base_params = [
        getattr(request, 'pasngrBe', None),
        getattr(request, 'cargoBe', None),
        getattr(request, 'startDePd', None),
        getattr(request, 'startDePd', None),
        getattr(request, 'endDePd', None),
        getattr(request, 'endDePd', None),
        getattr(request, 'airPort', None),
        getattr(request, 'pasngrBe', None),
        getattr(request, 'cargoBe', None),
        getattr(request, 'startDePd', None),
        getattr(request, 'startDePd', None),
        getattr(request, 'endDePd', None),
        getattr(request, 'endDePd', None),
        getattr(request, 'airPort', None),
    ]

    cond_query, params = build_conditions(request, [
        ('routeBe', "AND A_LINE = ?"),
        ('pasngrCargoBe', "AND A_USE = ?"),
        ('nvgBe', "AND a_REGULAR = ?"),
        ('routeBe', "AND A_LINE = ?"),
        ('pasngrCargoBe', "AND A_USE = ?"),
        ('nvgBe', "AND a_REGULAR = ?"),
    ])
    query += cond_query
    params = base_params + params

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [TransportStatsResponse(**row) for row in result]

async def fetch_airport_code(request: AirportCodeRequest, conn: aioodbc.Connection) -> List[AirportCodeResponse]:
    query = get_sql_query('get_airport_code')

    cond_query, params = build_conditions(request, [
        ('cityCode', "AND CITY_CODE = ?"),
        ('cityKor', "AND CITY_KOR = ?"),
        ('cityEng', "AND CITY_ENG = ?"),
        ('cityJpn', "AND CITY_JPN = ?"),
        ('cityChn', "AND CITY_CHN = ?"),
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [AirportCodeResponse(**row) for row in result]

async def fetch_bus(request: BusRequest, conn: aioodbc.Connection) -> List[BusResponse]:
    query = get_sql_query('get_bus')

    cond_query, params = build_conditions(request, [
        ('schAirport', "AND  c.SITE_NAME2 = UPPER(?)"),
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [BusResponse(**row) for row in result]

async def fetch_taxi_wait_cju(request: TaxiWaitCjuRequest, conn: aioodbc.Connection) -> List[TaxiWaitCjuResponse]:
    query = get_sql_query('get_taxi_wait_cju')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [TaxiWaitCjuResponse(**row) for row in result]

async def fetch_daily_expect_passenger(request: DailyExpectPassengerRequest, conn: aioodbc.Connection) -> List[DailyExpectPassengerResponse]:
    query = get_sql_query('get_daily_expect_passenger')

    cond_query, params = build_conditions(request, [
        ('schDate', "AND SDT = ?"),
        ('schAirport', "AND ARP = ?"),
        ('schTof', "AND TOF = ?"),
        ('schHH', "AND HH = ?"),
        ('schAOD', "AND AOD = ?"),
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [DailyExpectPassengerResponse(**row) for row in result]

async def fetch_low_visibility_idx(request: LowVisibilityIdxRequest, conn: aioodbc.Connection) -> List[LowVisibilityIdxResponse]:
    query = get_sql_query('get_low_visibility_idx')

    base_params = [getattr(request, 'idx', None)]

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query
    params = base_params + params

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [LowVisibilityIdxResponse(**row) for row in result]

async def fetch_epi_gh(request: EpiGhRequest, conn: aioodbc.Connection) -> List[EpiGhResponse]:
    query = get_sql_query('get_epi_gh')

    cond_query, params = build_conditions(request, [
        ('sdate', "AND A.BAS_YM >= ?"),
        ('edate', "AND A.BAS_YM <= ?"),
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [EpiGhResponse(**row) for row in result]

async def fetch_low_visibility(request: LowVisibilityRequest, conn: aioodbc.Connection) -> List[LowVisibilityResponse]:
    query = get_sql_query('get_low_visibility')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [LowVisibilityResponse(**row) for row in result]

async def fetch_low_visibility_latest(request: LowVisibilityLatestRequest, conn: aioodbc.Connection) -> List[LowVisibilityLatestResponse]:
    query = get_sql_query('get_low_visibility_latest')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [LowVisibilityLatestResponse(**row) for row in result]

async def fetch_retail_contract(request: RetailContractRequest, conn: aioodbc.Connection) -> List[RetailContractResponse]:
    query = get_sql_query('get_retail_contract')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [RetailContractResponse(**row) for row in result]

async def fetch_congestion_v1(request: CongestionV1Request, conn: aioodbc.Connection) -> List[CongestionV1Response]:
    query = get_sql_query('get_congestion_v1')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [CongestionV1Response(**row) for row in result]

async def fetch_congestion_v2(request: CongestionV2Request, conn: aioodbc.Connection) -> List[CongestionV2Response]:
    query = get_sql_query('get_congestion_v2')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [CongestionV2Response(**row) for row in result]

async def fetch_monthly_inout_cju(request: MonthlyInoutCjuRequest, conn: aioodbc.Connection) -> List[MonthlyInoutCjuResponse]:
    query = get_sql_query('get_monthly_inout_cju')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [MonthlyInoutCjuResponse(**row) for row in result]

async def fetch_wait_time_v1(request: WaitTimeV1Request, conn: aioodbc.Connection) -> List[WaitTimeV1Response]:
    query = get_sql_query('get_wait_time_v1')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [WaitTimeV1Response(**row) for row in result]

async def fetch_wait_time_v2(request: WaitTimeV2Request, conn: aioodbc.Connection) -> List[WaitTimeV2Response]:
    query = get_sql_query('get_wait_time_v2')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [WaitTimeV2Response(**row) for row in result]

