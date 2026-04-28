from fastapi import APIRouter, Depends
from typing import List
import aioodbc
from db.connection import get_connection
from .models import *
from . import service

router = APIRouter(prefix='/flight', tags=['flight'])

@router.get('/routes-info', response_model=List[RoutesInfoResponse])
async def get_routes_info(request: RoutesInfoRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_routes_info(request, conn)

@router.get('/aircraft-type', response_model=List[AircraftTypeResponse])
async def get_aircraft_type(request: AircraftTypeRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_aircraft_type(request, conn)

@router.get('/flight-status', response_model=List[FlightStatusResponse])
async def get_flight_status(request: FlightStatusRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_status(request, conn)

@router.get('/flight-status/taxfree', response_model=List[FlightStatusTaxfreeResponse])
async def get_flight_status_taxfree(request: FlightStatusTaxfreeRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_status_taxfree(request, conn)

@router.get('/flight-status/depart', response_model=List[FlightStatusDepartResponse])
async def get_flight_status_depart(request: FlightStatusDepartRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_status_depart(request, conn)

@router.get('/flight-status/arrival', response_model=List[FlightStatusArrivalResponse])
async def get_flight_status_arrival(request: FlightStatusArrivalRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_status_arrival(request, conn)

@router.get('/flight-schedule/taxfree-int', response_model=List[FlightScheduleTaxfreeIntResponse])
async def get_flight_schedule_taxfree_int(request: FlightScheduleTaxfreeIntRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_schedule_taxfree_int(request, conn)

@router.get('/flight-schedule/taxfree-dom', response_model=List[FlightScheduleTaxfreeDomResponse])
async def get_flight_schedule_taxfree_dom(request: FlightScheduleTaxfreeDomRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_schedule_taxfree_dom(request, conn)

@router.get('/apron/pus', response_model=List[ApronPusResponse])
async def get_apron_pus(request: ApronPusRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_apron_pus(request, conn)

@router.get('/apron/gmp', response_model=List[ApronGmpResponse])
async def get_apron_gmp(request: ApronGmpRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_apron_gmp(request, conn)

@router.get('/apron/cju', response_model=List[ApronCjuResponse])
async def get_apron_cju(request: ApronCjuRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_apron_cju(request, conn)

@router.get('/flight-schedule/dom', response_model=List[FlightScheduleDomResponse])
async def get_flight_schedule_dom(request: FlightScheduleDomRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_schedule_dom(request, conn)

@router.get('/flight-schedule/int', response_model=List[FlightScheduleIntResponse])
async def get_flight_schedule_int(request: FlightScheduleIntRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_schedule_int(request, conn)

@router.get('/flight-status/detail', response_model=List[FlightStatusDetailResponse])
async def get_flight_status_detail(request: FlightStatusDetailRequest = Depends(), conn: aioodbc.Connection = Depends(get_connection)):
    return await service.fetch_flight_status_detail(request, conn)

