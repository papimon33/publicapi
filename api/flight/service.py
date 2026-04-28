import os
import aioodbc
from typing import List, Dict
from .models import *
from core.utils import build_conditions, get_sql_query

async def fetch_routes_info(request: RoutesInfoRequest, conn: aioodbc.Connection) -> List[RoutesInfoResponse]:
    query = get_sql_query('get_routes_info')

    cond_query, params = build_conditions(request, [
        (('schEdDate', 'schStDate'), "AND TO_CHAR(DOMESTIC_STDATE,'yyyyMMdd') <= ? AND TO_CHAR(DOMESTIC_EDDATE,'yyyyMMdd') >= ?"),
        ((), "AND 1 != 1"),
        (('schEdDate', 'schStDate'), "AND TO_CHAR(INTERNATIONAL_STDATE,'yyyyMMdd') <= ? AND TO_CHAR(INTERNATIONAL_EDDATE,'yyyyMMdd') >= ?"),
        ((), "AND 1 != 1"),
        (('schEdDate', 'schStDate'), "AND TO_CHAR(INTERNATIONAL_STDATE,'yyyyMMdd') <= ? AND TO_CHAR(INTERNATIONAL_EDDATE,'yyyyMMdd') >= ?"),
        ((), "AND 1 != 1"),
        ('schAirport', "AND LINES.ARP = ?"),
        ('schLineType', "AND LINES.TOF = ?"),
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [RoutesInfoResponse(**row) for row in result]

async def fetch_aircraft_type(request: AircraftTypeRequest, conn: aioodbc.Connection) -> List[AircraftTypeResponse]:
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

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [AircraftTypeResponse(**row) for row in result]

async def fetch_flight_status(request: FlightStatusRequest, conn: aioodbc.Connection) -> List[FlightStatusResponse]:
    query = get_sql_query('get_flight_status')

    cond_query, params = build_conditions(request, [
        ('schAirCode', "AND T1.AIRPORT = ?"),
        (('schStTime', 'schEdTime'), "AND T1.STD BETWEEN ? AND ?"),
        ('schLineType', "AND T1.LINE = ?"),
        ('schIOType', "AND T1.IO = ?"),
        ('schFln', "AND T2.AIRLINE_CODE2||T1.Fln LIKE UPPER('%'||?||'%')"),
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [FlightStatusResponse(**row) for row in result]

async def fetch_flight_status_taxfree(request: FlightStatusTaxfreeRequest, conn: aioodbc.Connection) -> List[FlightStatusTaxfreeResponse]:
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

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [FlightStatusTaxfreeResponse(**row) for row in result]

async def fetch_flight_status_depart(request: FlightStatusDepartRequest, conn: aioodbc.Connection) -> List[FlightStatusDepartResponse]:
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

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [FlightStatusDepartResponse(**row) for row in result]

async def fetch_flight_status_arrival(request: FlightStatusArrivalRequest, conn: aioodbc.Connection) -> List[FlightStatusArrivalResponse]:
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

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [FlightStatusArrivalResponse(**row) for row in result]

async def fetch_flight_schedule_taxfree_int(request: FlightScheduleTaxfreeIntRequest, conn: aioodbc.Connection) -> List[FlightScheduleTaxfreeIntResponse]:
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

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [FlightScheduleTaxfreeIntResponse(**row) for row in result]

async def fetch_flight_schedule_taxfree_dom(request: FlightScheduleTaxfreeDomRequest, conn: aioodbc.Connection) -> List[FlightScheduleTaxfreeDomResponse]:
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

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [FlightScheduleTaxfreeDomResponse(**row) for row in result]

async def fetch_apron_pus(request: ApronPusRequest, conn: aioodbc.Connection) -> List[ApronPusResponse]:
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

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [ApronPusResponse(**row) for row in result]

async def fetch_apron_gmp(request: ApronGmpRequest, conn: aioodbc.Connection) -> List[ApronGmpResponse]:
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

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [ApronGmpResponse(**row) for row in result]

async def fetch_apron_cju(request: ApronCjuRequest, conn: aioodbc.Connection) -> List[ApronCjuResponse]:
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

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [ApronCjuResponse(**row) for row in result]

async def fetch_flight_schedule_dom(request: FlightScheduleDomRequest, conn: aioodbc.Connection) -> List[FlightScheduleDomResponse]:
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

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [FlightScheduleDomResponse(**row) for row in result]

async def fetch_flight_schedule_int(request: FlightScheduleIntRequest, conn: aioodbc.Connection) -> List[FlightScheduleIntResponse]:
    query = get_sql_query('get_flight_schedule_int')

    conditions = []
    params = []


    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [FlightScheduleIntResponse(**row) for row in result]

async def fetch_flight_status_detail(request: FlightStatusDetailRequest, conn: aioodbc.Connection) -> List[FlightStatusDetailResponse]:
    query = get_sql_query('get_flight_status_detail')

    conditions = []
    params = []


    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [FlightStatusDetailResponse(**row) for row in result]

