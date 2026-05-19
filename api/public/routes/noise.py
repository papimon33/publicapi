from fastapi import APIRouter, Depends
from core.models import PaginationResponse, PaginationParams
import aioodbc
from db.connection import get_connection
from api.public.models.noise import *
from api.public.services import noise as service

router = APIRouter(prefix='/noise', tags=['noise'])

@router.get('/noise-stats', response_model=PaginationResponse[NoiseStatsResponse])
async def get_noise_stats(request: NoiseStatsRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_noise_stats(request, page, conn)

@router.get('/noise-affected-area', response_model=PaginationResponse[NoiseAffectedAreaResponse])
async def get_noise_affected_area(request: NoiseAffectedAreaRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_noise_affected_area(request, page, conn)

@router.get('/noise-realtime/gmp', response_model=PaginationResponse[NoiseRealtimeGmpResponse])
async def get_noise_realtime_gmp(request: NoiseRealtimeGmpRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_noise_realtime_gmp(request, page, conn)

@router.get('/noise-realtime/pus', response_model=PaginationResponse[NoiseRealtimePusResponse])
async def get_noise_realtime_pus(request: NoiseRealtimePusRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_noise_realtime_pus(request, page, conn)
