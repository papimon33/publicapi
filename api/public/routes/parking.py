from fastapi import APIRouter, Depends
from core.models import PaginationResponse, PaginationParams
import aioodbc
from db.connection import get_connection
from api.public.models.parking import *
from api.public.services import parking as service

router = APIRouter(prefix='/parking', tags=['parking'])

@router.get('/valet-congestion', response_model=PaginationResponse[ValetCongestionResponse])
async def get_valet_congestion(request: ValetCongestionRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_valet_congestion(request, page, conn)

@router.get('/parking-congestion', response_model=PaginationResponse[ParkingCongestionResponse])
async def get_parking_congestion(request: ParkingCongestionRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_parking_congestion(request, page, conn)

@router.get('/parking-fee', response_model=PaginationResponse[ParkingFeeResponse])
async def get_parking_fee(request: ParkingFeeRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_parking_fee(request, page, conn)

@router.get('/airport-parking', response_model=PaginationResponse[AirportParkingResponse])
async def get_airport_parking(request: AirportParkingRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_airport_parking(request, page, conn)

@router.get('/parking-cell/gmp', response_model=PaginationResponse[ParkingCellGmpResponse])
async def get_parking_cell_gmp(request: ParkingCellGmpRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_parking_cell_gmp(request, page, conn)
