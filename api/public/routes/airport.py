from fastapi import APIRouter, Depends
from core.models import PaginationResponse, PaginationParams
import aioodbc
from db.connection import get_connection
from api.public.models.airport import *
from api.public.services import airport as service

router = APIRouter(prefix='/airport', tags=['airport'])

@router.get('/lease-contract/info', response_model=PaginationResponse[LeaseContractResponse])
async def get_lease_contract(request: LeaseContractRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_lease_contract(request, page, conn)

@router.get('/transport-stats/info', response_model=PaginationResponse[TransportStatsResponse])
async def get_transport_stats(request: TransportStatsRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_transport_stats(request, page, conn)

@router.get('/code/info', response_model=PaginationResponse[AirportCodeResponse])
async def get_airport_code(request: AirportCodeRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_airport_code(request, page, conn)

@router.get('/bus/info', response_model=PaginationResponse[BusResponse])
async def get_bus(request: BusRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_bus(request, page, conn)

@router.get('/taxi-wait/cju', response_model=PaginationResponse[TaxiWaitCjuResponse])
async def get_taxi_wait_cju(request: TaxiWaitCjuRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_taxi_wait_cju(request, page, conn)

@router.get('/daily-expect-passenger/info', response_model=PaginationResponse[DailyExpectPassengerResponse])
async def get_daily_expect_passenger(request: DailyExpectPassengerRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_daily_expect_passenger(request, page, conn)

@router.get('/low-visibility/idx', response_model=PaginationResponse[LowVisibilityIdxResponse])
async def get_low_visibility_idx(request: LowVisibilityIdxRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_low_visibility_idx(request, page, conn)

@router.get('/epi-gh/info', response_model=PaginationResponse[EpiGhResponse])
async def get_epi_gh(request: EpiGhRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_epi_gh(request, page, conn)

@router.get('/low-visibility/info', response_model=PaginationResponse[LowVisibilityResponse])
async def get_low_visibility(request: LowVisibilityRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_low_visibility(request, page, conn)

@router.get('/low-visibility/latest', response_model=PaginationResponse[LowVisibilityLatestResponse])
async def get_low_visibility_latest(request: LowVisibilityLatestRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_low_visibility_latest(request, page, conn)

@router.get('/retail-contract/info', response_model=PaginationResponse[RetailContractResponse])
async def get_retail_contract(request: RetailContractRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_retail_contract(request, page, conn)

@router.get('/congestion/v1', response_model=PaginationResponse[CongestionV1Response])
async def get_congestion_v1(request: CongestionV1Request = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_congestion_v1(request, page, conn)

@router.get('/congestion/v2', response_model=PaginationResponse[CongestionV2Response])
async def get_congestion_v2(request: CongestionV2Request = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_congestion_v2(request, page, conn)

@router.get('/montly-inout/cju', response_model=PaginationResponse[MonthlyInoutCjuResponse])
async def get_monthly_inout_cju(request: MonthlyInoutCjuRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_monthly_inout_cju(request, page, conn)

@router.get('/process-time/v1', response_model=PaginationResponse[ProcessTimeV1Response])
async def get_process_time_v1(request: ProcessTimeV1Request = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_process_time_v1(request, page, conn)

@router.get('/process-time/v2', response_model=PaginationResponse[ProcessTimeV2Response])
async def get_process_time_v2(request: ProcessTimeV2Request = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_process_time_v2(request, page, conn)

