from fastapi import APIRouter, Depends
from core.models import PaginationResponse, PaginationParams
import aioodbc
from db.connection import get_connection
from api.public.models.parking import *
from api.public.services import parking as service

router = APIRouter(prefix='/parking', tags=['parking'])

@router.get('/valet-congestion/gmp-dom', response_model=PaginationResponse[ValetCongestionGmpDomResponse])
async def get_valet_congestion_gmp_dom(request: ValetCongestionGmpDomRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_valet_congestion_gmp_dom(request, page, conn)

@router.get('/congestion/info', response_model=PaginationResponse[ParkingCongestionResponse])
async def get_parking_congestion(request: ParkingCongestionRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_parking_congestion(request, page, conn)

@router.get('/fee/info', response_model=PaginationResponse[ParkingFeeResponse])
async def get_parking_fee(request: ParkingFeeRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_parking_fee(request, page, conn)

@router.get('/realtime-status/info', response_model=PaginationResponse[AirportParkingResponse])
async def get_airport_parking(request: AirportParkingRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_airport_parking(request, page, conn)

@router.get('/available-spaces/gmp-int-indoor', response_model=PaginationResponse[AvailableSpacesGmpIntIndoorResponse])
async def get_available_spaces_gmp_int_indoor(request: AvailableSpacesGmpIntIndoorRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_available_spaces_gmp_int_indoor(request, page, conn)
