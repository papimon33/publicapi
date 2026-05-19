import os
import aioodbc
from typing import List, Dict, Any, Tuple
from api.public.models.airport import *
from core.models import PaginationResponse, PaginationParams
from core.utils import build_conditions, get_sql_query, wrap_pagenation_sql, execute_query


def _build_body(data, page, total_count):
    return {
        "data": data,
        "numOfRows": page.numOfRows,
        "pageNo": page.pageNo,
        "totalCount": total_count,
    }


async def fetch_lease_contract(request: LeaseContractRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[LeaseContractResponse]:
    query = get_sql_query('get_lease_contract')
    cond_query, params = build_conditions(request, [])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[LeaseContractResponse](body=_build_body([LeaseContractResponse(**row) for row in result], page, total_count))

async def fetch_transport_stats(request: TransportStatsRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[TransportStatsResponse]:
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
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[TransportStatsResponse](body=_build_body([TransportStatsResponse(**row) for row in result], page, total_count))

async def fetch_airport_code(request: AirportCodeRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[AirportCodeResponse]:
    query = get_sql_query('get_airport_code')
    cond_query, params = build_conditions(request, [
        ('cityCode', "AND CITY_CODE = ?"),
        ('cityKor', "AND CITY_KOR = ?"),
        ('cityEng', "AND CITY_ENG = ?"),
        ('cityJpn', "AND CITY_JPN = ?"),
        ('cityChn', "AND CITY_CHN = ?"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[AirportCodeResponse](body=_build_body([AirportCodeResponse(**row) for row in result], page, total_count))

async def fetch_bus(request: BusRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[BusResponse]:
    query = get_sql_query('get_bus')
    cond_query, params = build_conditions(request, [
        ('schAirport', "AND  c.SITE_NAME2 = UPPER(?)"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[BusResponse](body=_build_body([BusResponse(**row) for row in result], page, total_count))

async def fetch_taxi_wait_cju(request: TaxiWaitCjuRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[TaxiWaitCjuResponse]:
    query = get_sql_query('get_taxi_wait_cju')
    cond_query, params = build_conditions(request, [])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[TaxiWaitCjuResponse](body=_build_body([TaxiWaitCjuResponse(**row) for row in result], page, total_count))

async def fetch_daily_expect_passenger(request: DailyExpectPassengerRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[DailyExpectPassengerResponse]:
    query = get_sql_query('get_daily_expect_passenger')
    cond_query, params = build_conditions(request, [
        ('schDate', "AND SDT = ?"),
        ('schAirport', "AND ARP = ?"),
        ('schTof', "AND TOF = ?"),
        ('schHH', "AND HH = ?"),
        ('schAOD', "AND AOD = ?"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[DailyExpectPassengerResponse](body=_build_body([DailyExpectPassengerResponse(**row) for row in result], page, total_count))

async def fetch_low_visibility_idx(request: LowVisibilityIdxRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[LowVisibilityIdxResponse]:
    query = get_sql_query('get_low_visibility_idx')
    base_params = [getattr(request, 'idx', None)]
    cond_query, params = build_conditions(request, [])
    query += cond_query
    params = base_params + params
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[LowVisibilityIdxResponse](body=_build_body([LowVisibilityIdxResponse(**row) for row in result], page, total_count))

async def fetch_epi_gh(request: EpiGhRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[EpiGhResponse]:
    query = get_sql_query('get_epi_gh')
    cond_query, params = build_conditions(request, [
        ('sdate', "AND A.BAS_YM >= ?"),
        ('edate', "AND A.BAS_YM <= ?"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[EpiGhResponse](body=_build_body([EpiGhResponse(**row) for row in result], page, total_count))

async def fetch_low_visibility(request: LowVisibilityRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[LowVisibilityResponse]:
    query = get_sql_query('get_low_visibility')
    cond_query, params = build_conditions(request, [])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[LowVisibilityResponse](body=_build_body([LowVisibilityResponse(**row) for row in result], page, total_count))

async def fetch_low_visibility_latest(request: LowVisibilityLatestRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[LowVisibilityLatestResponse]:
    query = get_sql_query('get_low_visibility_latest')
    cond_query, params = build_conditions(request, [])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[LowVisibilityLatestResponse](body=_build_body([LowVisibilityLatestResponse(**row) for row in result], page, total_count))

async def fetch_retail_contract(request: RetailContractRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[RetailContractResponse]:
    query = get_sql_query('get_retail_contract')
    cond_query, params = build_conditions(request, [])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[RetailContractResponse](body=_build_body([RetailContractResponse(**row) for row in result], page, total_count))

async def fetch_congestion_v1(request: CongestionV1Request, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[CongestionV1Response]:
    query = get_sql_query('get_congestion_v1')
    cond_query, params = build_conditions(request, [])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[CongestionV1Response](body=_build_body([CongestionV1Response(**row) for row in result], page, total_count))

async def fetch_congestion_v2(request: CongestionV2Request, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[CongestionV2Response]:
    query = get_sql_query('get_congestion_v2')
    cond_query, params = build_conditions(request, [])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[CongestionV2Response](body=_build_body([CongestionV2Response(**row) for row in result], page, total_count))

async def fetch_monthly_inout_cju(request: MonthlyInoutCjuRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[MonthlyInoutCjuResponse]:
    query = get_sql_query('get_monthly_inout_cju')
    cond_query, params = build_conditions(request, [])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[MonthlyInoutCjuResponse](body=_build_body([MonthlyInoutCjuResponse(**row) for row in result], page, total_count))

async def fetch_wait_time_v1(request: WaitTimeV1Request, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[WaitTimeV1Response]:
    query = get_sql_query('get_wait_time_v1')
    cond_query, params = build_conditions(request, [])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[WaitTimeV1Response](body=_build_body([WaitTimeV1Response(**row) for row in result], page, total_count))

async def fetch_wait_time_v2(request: WaitTimeV2Request, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[WaitTimeV2Response]:
    query = get_sql_query('get_wait_time_v2')
    cond_query, params = build_conditions(request, [])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[WaitTimeV2Response](body=_build_body([WaitTimeV2Response(**row) for row in result], page, total_count))
