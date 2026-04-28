import os
import aioodbc
from typing import List, Dict, Any, Tuple
from .models import *
from core.utils import build_conditions, get_sql_query

async def fetch_noise_stats(request: NoiseStatsRequest, conn: aioodbc.Connection) -> List[NoiseStatsResponse]:
    query = get_sql_query('get_noise_stats')

    base_params = [getattr(request, 'year', None)] * 13

    cond_query, params = build_conditions(request, [
        ('airportCode', "AND T1.ARP_SE = ?"),
    ])
    query += cond_query
    params = base_params + params

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [NoiseStatsResponse(**row) for row in result]

async def fetch_noise_affected_area(request: NoiseAffectedAreaRequest, conn: aioodbc.Connection) -> List[NoiseAffectedAreaResponse]:
    query = get_sql_query('get_noise_affected_area')

    base_params = [
        getattr(request, 'city1', None),
        getattr(request, 'city2', None),
        getattr(request, 'dong', None)
    ] * 10

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

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [NoiseAffectedAreaResponse(**row) for row in result]

async def fetch_noise_realtime_gmp(request: NoiseRealtimeGmpRequest, conn: aioodbc.Connection) -> List[NoiseRealtimeGmpResponse]:
    query = get_sql_query('get_noise_realtime_gmp')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [NoiseRealtimeGmpResponse(**row) for row in result]

async def fetch_noise_realtime_pus(request: NoiseRealtimePusRequest, conn: aioodbc.Connection) -> List[NoiseRealtimePusResponse]:
    query = get_sql_query('get_noise_realtime_pus')

    cond_query, params = build_conditions(request, [
    ])
    query += cond_query

    async with conn.cursor() as cursor:
        await cursor.execute(query, params)
        rows = await cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return [NoiseRealtimePusResponse(**row) for row in result]

