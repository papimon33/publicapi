from fastapi import APIRouter, Depends
from core.models import PaginationResponse, PaginationParams
import aioodbc
from db.connection import get_connection
from api.public.models.flight import *
from api.public.services import flight as service

router = APIRouter(prefix='/flight', tags=['flight'])

@router.get('/routes/info', response_model=PaginationResponse[RoutesInfoResponse])
async def get_routes_info(request: RoutesInfoRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_routes_info(request, page, conn)

@router.get('/aircraft-status/info', response_model=PaginationResponse[AircraftStatusResponse])
async def get_aircraft_status(request: AircraftStatusRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_aircraft_status(request, page, conn)

@router.get('/status/info', response_model=PaginationResponse[FlightStatusResponse])
async def get_flight_status(request: FlightStatusRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_status(request, page, conn)

@router.get('/status/taxfree', response_model=PaginationResponse[FlightStatusTaxfreeResponse])
async def get_flight_status_taxfree(request: FlightStatusTaxfreeRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_status_taxfree(request, page, conn)

@router.get('/status/depart', response_model=PaginationResponse[FlightStatusDepartResponse])
async def get_flight_status_depart(request: FlightStatusDepartRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_status_depart(request, page, conn)

@router.get('/status/arrival', response_model=PaginationResponse[FlightStatusArrivalResponse])
async def get_flight_status_arrival(request: FlightStatusArrivalRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_status_arrival(request, page, conn)

@router.get('/status/detail', response_model=PaginationResponse[FlightStatusDetailResponse])
async def get_flight_status_detail(request: FlightStatusDetailRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_status_detail(request, page, conn)

@router.get('/schedule/taxfree-int', response_model=PaginationResponse[FlightScheduleTaxfreeIntResponse])
async def get_flight_schedule_taxfree_int(request: FlightScheduleTaxfreeIntRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_schedule_taxfree_int(request, page, conn)

@router.get('/schedule/taxfree-dom', response_model=PaginationResponse[FlightScheduleTaxfreeDomResponse])
async def get_flight_schedule_taxfree_dom(request: FlightScheduleTaxfreeDomRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_schedule_taxfree_dom(request, page, conn)

@router.get('/schedule/dom', response_model=PaginationResponse[FlightScheduleDomResponse])
async def get_flight_schedule_dom(request: FlightScheduleDomRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_schedule_dom(request, page, conn)

@router.get('/schedule/int', response_model=PaginationResponse[FlightScheduleIntResponse])
async def get_flight_schedule_int(request: FlightScheduleIntRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_schedule_int(request, page, conn)

@router.get('/apron-status/pus', response_model=PaginationResponse[ApronPusResponse])
async def get_apron_pus(request: ApronPusRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_apron_pus(request, page, conn)

@router.get('/apron-status/gmp', response_model=PaginationResponse[ApronGmpResponse])
async def get_apron_gmp(request: ApronGmpRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_apron_gmp(request, page, conn)

@router.get('/apron-status/cju', response_model=PaginationResponse[ApronCjuResponse])
async def get_apron_cju(request: ApronCjuRequest = Depends(), page: PaginationParams = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_apron_cju(request, page, conn)
