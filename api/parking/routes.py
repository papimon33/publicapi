from fastapi import APIRouter, Depends
from typing import List
import aioodbc
from db.connection import get_connection
from .models import *
from . import service

router = APIRouter(prefix='/parking', tags=['parking'])

@router.get('/valet-congestion', response_model=List[ValetCongestionResponse])
async def get_valet_congestion(request: ValetCongestionRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_valet_congestion(request, conn)

@router.get('/parking-congestion', response_model=List[ParkingCongestionResponse])
async def get_parking_congestion(request: ParkingCongestionRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_parking_congestion(request, conn)

@router.get('/parking-fee', response_model=List[ParkingFeeResponse])
async def get_parking_fee(request: ParkingFeeRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_parking_fee(request, conn)

@router.get('/airport-parking', response_model=List[AirportParkingResponse])
async def get_airport_parking(request: AirportParkingRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_airport_parking(request, conn)

@router.get('/parking-cell/gmp', response_model=List[ParkingCellGmpResponse])
async def get_parking_cell_gmp(request: ParkingCellGmpRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_parking_cell_gmp(request, conn)

