from fastapi import APIRouter, Depends
from typing import List
import aioodbc
from db.connection import get_connection
from .models import *
from . import service

router = APIRouter(prefix='/noise', tags=['noise'])

@router.get('/noise-stats', response_model=List[NoiseStatsResponse])
async def get_noise_stats(request: NoiseStatsRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_noise_stats(request, conn)

@router.get('/noise-affected-area', response_model=List[NoiseAffectedAreaResponse])
async def get_noise_affected_area(request: NoiseAffectedAreaRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_noise_affected_area(request, conn)

@router.get('/noise-realtime/gmp', response_model=List[NoiseRealtimeGmpResponse])
async def get_noise_realtime_gmp(request: NoiseRealtimeGmpRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_noise_realtime_gmp(request, conn)

@router.get('/noise-realtime/pus', response_model=List[NoiseRealtimePusResponse])
async def get_noise_realtime_pus(request: NoiseRealtimePusRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_noise_realtime_pus(request, conn)

