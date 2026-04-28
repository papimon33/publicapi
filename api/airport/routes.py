from fastapi import APIRouter, Depends
from typing import List
import aioodbc
from db.connection import get_connection
from .models import *
from . import service

router = APIRouter(prefix='/airport', tags=['airport'])

@router.get('/lease-contract', response_model=List[LeaseContractResponse])
async def get_lease_contract(request: LeaseContractRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_lease_contract(request, conn)

@router.get('/transport-stats', response_model=List[TransportStatsResponse])
async def get_transport_stats(request: TransportStatsRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_transport_stats(request, conn)

@router.get('/airport-code', response_model=List[AirportCodeResponse])
async def get_airport_code(request: AirportCodeRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_airport_code(request, conn)

@router.get('/bus', response_model=List[BusResponse])
async def get_bus(request: BusRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_bus(request, conn)

@router.get('/taxi-wait-cju', response_model=List[TaxiWaitCjuResponse])
async def get_taxi_wait_cju(request: TaxiWaitCjuRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_taxi_wait_cju(request, conn)

@router.get('/daily-expect-passenger', response_model=List[DailyExpectPassengerResponse])
async def get_daily_expect_passenger(request: DailyExpectPassengerRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_daily_expect_passenger(request, conn)

@router.get('/low-visibility/idx', response_model=List[LowVisibilityIdxResponse])
async def get_low_visibility_idx(request: LowVisibilityIdxRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_low_visibility_idx(request, conn)

@router.get('/epi-gh', response_model=List[EpiGhResponse])
async def get_epi_gh(request: EpiGhRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_epi_gh(request, conn)

@router.get('/low-visibility', response_model=List[LowVisibilityResponse])
async def get_low_visibility(request: LowVisibilityRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_low_visibility(request, conn)

@router.get('/low-visibility/latest', response_model=List[LowVisibilityLatestResponse])
async def get_low_visibility_latest(request: LowVisibilityLatestRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_low_visibility_latest(request, conn)

@router.get('/retail-contract', response_model=List[RetailContractResponse])
async def get_retail_contract(request: RetailContractRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_retail_contract(request, conn)

@router.get('/congestion/v1', response_model=List[CongestionV1Response])
async def get_congestion_v1(request: CongestionV1Request = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_congestion_v1(request, conn)

@router.get('/congestion/v2', response_model=List[CongestionV2Response])
async def get_congestion_v2(request: CongestionV2Request = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_congestion_v2(request, conn)

@router.get('/monthly-inout/cju', response_model=List[MonthlyInoutCjuResponse])
async def get_monthly_inout_cju(request: MonthlyInoutCjuRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_monthly_inout_cju(request, conn)

@router.get('/wait-time/v1', response_model=List[WaitTimeV1Response])
async def get_wait_time_v1(request: WaitTimeV1Request = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_wait_time_v1(request, conn)

@router.get('/wait-time/v2', response_model=List[WaitTimeV2Response])
async def get_wait_time_v2(request: WaitTimeV2Request = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_wait_time_v2(request, conn)

