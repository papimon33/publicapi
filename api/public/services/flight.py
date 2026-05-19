import os
import aioodbc
from typing import List, Dict
from api.public.models.flight import *
from core.models import PaginationResponse, PaginationParams
from core.utils import build_conditions, get_sql_query, wrap_pagenation_sql, execute_query

def _build_body(data, page, total_count):
    return {"data": data, "numOfRows": page.numOfRows, "pageNo": page.pageNo, "totalCount": total_count}

async def fetch_routes_info(request: RoutesInfoRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[RoutesInfoResponse]:
    query = get_sql_query('get_routes_info')
    cond_query, params = build_conditions(request, [
        (('schEdDate', 'schStDate'), "AND TO_CHAR(DOMESTIC_STDATE,'yyyyMMdd') <= ? AND TO_CHAR(DOMESTIC_EDDATE,'yyyyMMdd') >= ?"),
        (('schEdDate', 'schStDate'), "AND TO_CHAR(INTERNATIONAL_STDATE,'yyyyMMdd') <= ? AND TO_CHAR(INTERNATIONAL_EDDATE,'yyyyMMdd') >= ?"),
        (('schEdDate', 'schStDate'), "AND TO_CHAR(INTERNATIONAL_STDATE,'yyyyMMdd') <= ? AND TO_CHAR(INTERNATIONAL_EDDATE,'yyyyMMdd') >= ?"),
        ('schAirport', "AND LINES.ARP = ?"),
        ('schLineType', "AND LINES.TOF = ?"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[RoutesInfoResponse](body=_build_body([RoutesInfoResponse(**r) for r in result], page, total_count))

async def fetch_aircraft_type(request: AircraftTypeRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[AircraftTypeResponse]:
    query = get_sql_query('get_aircraft_type')
    cond_query, params = build_conditions(request, [
        ('schAirCode', "AND T1.AIRPORT = ?"),
        (('schStTime', 'schEdTime'), "AND T1.ACT_C_DATE||T1.STD BETWEEN ? AND ?"),
        ('Line', "AND T1.LINE = UPPER(?)"),
        ('schIOType', "AND T1.IO = UPPER(?)"),
        ('schFln', "AND T2.AIRLINE_CODE2||T1.Fln LIKE UPPER('%'||?||'%')"),
        ('schFID', "AND FID = ?"),
        ('schAPLno', "AND APL_REG_NO= ?"),
        ('schAPM', "AND T1.ICAO_APM_CD = ?"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[AircraftTypeResponse](body=_build_body([AircraftTypeResponse(**r) for r in result], page, total_count))

async def fetch_flight_status(request: FlightStatusRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[FlightStatusResponse]:
    query = get_sql_query('get_flight_status')
    cond_query, params = build_conditions(request, [
        ('schAirCode', "AND T1.AIRPORT = ?"),
        (('schStTime', 'schEdTime'), "AND T1.STD BETWEEN ? AND ?"),
        ('schLineType', "AND T1.LINE = ?"),
        ('schIOType', "AND T1.IO = ?"),
        ('schFln', "AND T2.AIRLINE_CODE2||T1.Fln LIKE UPPER('%'||?||'%')"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[FlightStatusResponse](body=_build_body([FlightStatusResponse(**r) for r in result], page, total_count))

async def fetch_flight_status_taxfree(request: FlightStatusTaxfreeRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[FlightStatusTaxfreeResponse]:
    query = get_sql_query('get_flight_status_taxfree')
    cond_query, params = build_conditions(request, [
        ('searchDate', "AND SUBSTR(scheduledatetime,1,8) = ?"),
        ('searchFrom', "AND SUBSTR(scheduledatetime,9,4) >= ?"),
        ('searchTo', "AND SUBSTR(scheduledatetime,9,4) <= ?"),
        ('fid', "AND fid = ?"),
        ('flightId', "AND flightId = UPPER (?)"),
        ('depCityCode', "AND depCityCode = UPPER(?)"),
        ('depCity', "AND depCity LIKE '%'|| ? ||'%'"),
        ('arrvCityCode', "AND arrvCityCode = UPPER (?)"),
        ('arrvCity', "AND arrvCity LIKE '%'|| ? ||'%'"),
        ('fgenType', "AND fgenType = UPPER (?)"),
        ('fgenTime', "AND fgenTime >= ?"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[FlightStatusTaxfreeResponse](body=_build_body([FlightStatusTaxfreeResponse(**r) for r in result], page, total_count))

async def fetch_flight_status_depart(request: FlightStatusDepartRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[FlightStatusDepartResponse]:
    query = get_sql_query('get_flight_status_depart')
    cond_query, params = build_conditions(request, [
        ('searchday', "AND searchday = ?"),
        ('from_time', "AND SUBSTR(SCHEDULEDATETIME,9,4) >= ?"),
        ('to_time', "AND SUBSTR(SCHEDULEDATETIME,9,4) <= ?"),
        ('airport_code', "AND DEP_AIRPORT_CODE = UPPER(?)"),
        ('airport', "AND DEP_AIRPORT LIKE '%'|| ? ||'%'"),
        ('arr_airport_code', "AND ARR_AIRPORT_CODE = UPPER (?)"),
        ('arr_airport', "AND ARR_AIRPORT LIKE '%'|| ? ||'%'"),
        ('fgenTime', "AND fgenTime >= ?"),
        ('f_id', "AND FID = ?"),
        ('flight_id', "AND FLIGHTID = UPPER (?)"),
        ('line', "AND (CASE WHEN LINE = '국내' THEN 'D' WHEN LINE = '국제' THEN 'I' ELSE LINE END = UPPER (?) )"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[FlightStatusDepartResponse](body=_build_body([FlightStatusDepartResponse(**r) for r in result], page, total_count))

async def fetch_flight_status_arrival(request: FlightStatusArrivalRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[FlightStatusArrivalResponse]:
    query = get_sql_query('get_flight_status_arrival')
    cond_query, params = build_conditions(request, [
        ('searchday', "AND searchday = ?"),
        ('from_time', "AND SUBSTR(SCHEDULEDATETIME,9,4) >= ?"),
        ('to_time', "AND SUBSTR(SCHEDULEDATETIME,9,4) <= ?"),
        ('airport_code', "AND ARR_AIRPORT_CODE = UPPER(?)"),
        ('airport', "AND ARR_AIRPORT LIKE '%'|| ? ||'%'"),
        ('dep_airport_code', "AND dep_AIRPORT_CODE = UPPER (?)"),
        ('dep_airport', "AND dep_AIRPORT LIKE '%'|| ? ||'%'"),
        ('fgenTime', "AND fgenTime >= ?"),
        ('f_id', "AND FID = ?"),
        ('flight_id', "AND FLIGHTID = UPPER (?)"),
        ('line', "AND (CASE WHEN LINE = '국내' THEN 'D' WHEN LINE = '국제' THEN 'I' ELSE LINE END = UPPER (?) )"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[FlightStatusArrivalResponse](body=_build_body([FlightStatusArrivalResponse(**r) for r in result], page, total_count))

async def fetch_flight_schedule_taxfree_int(request: FlightScheduleTaxfreeIntRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[FlightScheduleTaxfreeIntResponse]:
    query = get_sql_query('get_flight_schedule_taxfree_int')
    cond_query, params = build_conditions(request, [
        ('fid', "AND FID = ?"),
        ('fgenTime', "AND fgenTime >= ?"),
        ('flightId', "AND flightId = UPPER (?)"),
        ('depCityCode', "AND depCityCode = UPPER(?)"),
        ('depCity', "AND depCity LIKE '%'|| ? ||'%'"),
        ('arrvCityCode', "AND arrvCityCode = UPPER (?)"),
        ('arrvCity', "AND arrvCity LIKE '%'|| ? ||'%'"),
        ('fgenType', "AND fgenType = UPPER (?)"),
        ('schAirLine', "AND airlinecode= UPPER (?)"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[FlightScheduleTaxfreeIntResponse](body=_build_body([FlightScheduleTaxfreeIntResponse(**r) for r in result], page, total_count))

async def fetch_flight_schedule_taxfree_dom(request: FlightScheduleTaxfreeDomRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[FlightScheduleTaxfreeDomResponse]:
    query = get_sql_query('get_flight_schedule_taxfree_dom')
    cond_query, params = build_conditions(request, [
        ('fid', "AND FID = ?"),
        ('fgenTime', "AND fgenTime >= ?"),
        ('flightId', "AND flightId = UPPER (?)"),
        ('depCityCode', "AND depCityCode = UPPER(?)"),
        ('depCity', "AND depCity LIKE '%'|| ? ||'%'"),
        ('arrvCityCode', "AND arrvCityCode = UPPER (?)"),
        ('arrvCity', "AND arrvCity LIKE '%'|| ? ||'%'"),
        ('fgenType', "AND fgenType = UPPER (?)"),
        ('schAirLine', "AND airlinecode= UPPER (?)"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[FlightScheduleTaxfreeDomResponse](body=_build_body([FlightScheduleTaxfreeDomResponse(**r) for r in result], page, total_count))

async def fetch_apron_pus(request: ApronPusRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[ApronPusResponse]:
    query = get_sql_query('get_apron_pus')
    cond_query, params = build_conditions(request, [
        ('flightdate', "AND TO_CHAR(T1.ACT_DATE, 'yyyymmdd') = ?"),
        ('airport', "AND T1.AIRPORT = ?"),
        ('std', "AND T1.STD = ?"),
        ('etd', "AND T1.ETD = ?"),
        ('line', "AND T1.LINE = ?"),
        ('io', "AND T1.IO = ?"),
        ('airfln', "AND T2.AIRLINE_CODE2||T1.Fln LIKE UPPER('%'||?||'%')"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[ApronPusResponse](body=_build_body([ApronPusResponse(**r) for r in result], page, total_count))

async def fetch_apron_gmp(request: ApronGmpRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[ApronGmpResponse]:
    query = get_sql_query('get_apron_gmp')
    cond_query, params = build_conditions(request, [
        ('FLIGHT_DATE', "AND TO_CHAR(T1.ACT_DATE, 'yyyymmdd') = ?"),
        ('AIRPORT', "AND T1.AIRPORT = ?"),
        ('STD', "AND T1.STD = ?"),
        ('ETD', "AND T1.ETD = ?"),
        ('LINE', "AND T1.LINE = ?"),
        ('IO', "AND T1.IO = ?"),
        ('AIR_FLN', "AND T2.AIRLINE_CODE2||T1.Fln LIKE UPPER('%'||?||'%')"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[ApronGmpResponse](body=_build_body([ApronGmpResponse(**r) for r in result], page, total_count))

async def fetch_apron_cju(request: ApronCjuRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[ApronCjuResponse]:
    query = get_sql_query('get_apron_cju')
    cond_query, params = build_conditions(request, [
        ('FLIGHT_DATE', "AND TO_CHAR(T1.ACT_DATE, 'yyyymmdd') = ?"),
        ('AIRPORT', "AND T1.AIRPORT = ?"),
        ('STD', "AND T1.STD = ?"),
        ('ETD', "AND T1.ETD = ?"),
        ('LINE', "AND T1.LINE = ?"),
        ('IO', "AND T1.IO = ?"),
        ('AIR_FLN', "AND T2.AIRLINE_CODE2||T1.Fln LIKE UPPER('%'||?||'%')"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[ApronCjuResponse](body=_build_body([ApronCjuResponse(**r) for r in result], page, total_count))

async def fetch_flight_schedule_dom(request: FlightScheduleDomRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[FlightScheduleDomResponse]:
    query = get_sql_query('get_flight_schedule_dom')
    cond_query, params = build_conditions(request, [
        ('schDate', "AND TO_CHAR(DOMESTIC_STDATE, 'yyyymmdd') <= ?"),
        ('schDate', "AND TO_CHAR(DOMESTIC_EDDATE, 'yyyymmdd') >= ?"),
        ('schDeptCityCode', "AND A.DOMESTIC_START_CITY = ?"),
        ('schArrvCityCode', "AND A.DOMESTIC_ARRIVAL_CITY = ?"),
        ('schAirLine', "AND SUBSTR(DOMESTIC_NUM, 0, 2) = ?"),
        ('schFlightNum', "AND DOMESTIC_NUM LIKE '%'||?||'%'"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[FlightScheduleDomResponse](body=_build_body([FlightScheduleDomResponse(**r) for r in result], page, total_count))

async def fetch_flight_schedule_int(request: FlightScheduleIntRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[FlightScheduleIntResponse]:
    query = get_sql_query('get_flight_schedule_int')
    cond_query, params = build_conditions(request, [
        ('schDate', "AND TO_CHAR(INTERNATIONAL_STDATE, 'yyyymmdd') <= ?"),
        ('schDate', "AND TO_CHAR(INTERNATIONAL_EDDATE, 'yyyymmdd') >= ?"),
        ('schDeptCityCode', "AND DECODE(A.INTERNATIONAL_IO_TYPE, 'IN', A.INTERNATIONAL_AIRPORT_INTE, A.INTERNATIONAL_AIRPORT_DOME) = UPPER(?)"),
        ('schArrvCityCode', "AND DECODE(A.INTERNATIONAL_IO_TYPE, 'IN', A.INTERNATIONAL_AIRPORT_DOME, A.INTERNATIONAL_AIRPORT_INTE) = UPPER(?)"),
        ('schAirLine', "AND SUBSTR(INTERNATIONAL_NUM, 0, 2) = ?"),
        ('schFlightNum', "AND UPPER(INTERNATIONAL_NUM) LIKE '%'||?||'%'"),
    ])
    query += cond_query
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[FlightScheduleIntResponse](body=_build_body([FlightScheduleIntResponse(**r) for r in result], page, total_count))

async def fetch_flight_status_detail(request: FlightStatusDetailRequest, page: PaginationParams, conn: aioodbc.Connection) -> PaginationResponse[FlightStatusDetailResponse]:
    query = get_sql_query('get_flight_status_detail')
    params = []
    count_query, paginated_query = wrap_pagenation_sql(query, page)
    total_count, result = await execute_query(conn, count_query, paginated_query, params)
    return PaginationResponse[FlightStatusDetailResponse](body=_build_body([FlightStatusDetailResponse(**r) for r in result], page, total_count))
