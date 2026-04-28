from pydantic import BaseModel
from typing import Optional, List

class FlightStatusTaxfreeRequest(BaseModel):
    schStTime: Optional[str] = None
    schEdTime: Optional[str] = None
    schLineType: Optional[str] = None
    schIOType: Optional[str] = None
    schAirCode: Optional[str] = None
    serviceKey: Optional[str] = None
    schFln: Optional[str] = None
    schRmk: Optional[str] = None

class FlightStatusTaxfreeResponse(BaseModel):
    BOARDING_KOR: Optional[str] = None
    BOARDING_ENG: Optional[str] = None
    ARRIVED_KOR: Optional[str] = None
    ARRIVED_ENG: Optional[str] = None
    AIR_FLN: Optional[str] = None
    LINE: Optional[str] = None

class RoutesInfoRequest(BaseModel):
    schStDate: Optional[str] = None
    schEdDate: Optional[str] = None
    schLineType: Optional[str] = None
    schAirport: Optional[str] = None
    serviceKey: Optional[str] = None

class RoutesInfoResponse(BaseModel):
    ARP: Optional[str] = None
    ODP: Optional[str] = None
    TOF: Optional[str] = None
    KM: Optional[str] = None
    TIME: Optional[str] = None

class AircraftTypeRequest(BaseModel):
    pass

class AircraftTypeResponse(BaseModel):
    pass

class FlightStatusDepartRequest(BaseModel):
    searchday: Optional[str] = None
    from_time: Optional[str] = None
    to_time: Optional[str] = None
    airport_code: Optional[str] = None
    f_id: Optional[str] = None
    flight_id: Optional[str] = None
    line: Optional[str] = None
    serviceKey: Optional[str] = None
    airport: Optional[str] = None
    arr_airport_code: Optional[str] = None
    arr_airport: Optional[str] = None
    fgenTime: Optional[str] = None

class FlightStatusDepartResponse(BaseModel):
    FGENTIME: Optional[str] = None
    SEARCHDAY: Optional[str] = None
    SCHEDULEDATETIME: Optional[str] = None
    ESTIMATEDDATETIME: Optional[str] = None
    AIRLINE: Optional[str] = None
    CODESHARE: Optional[str] = None
    MASTERFLIGHTID: Optional[str] = None
    FLIGHTID: Optional[str] = None
    LINE: Optional[str] = None
    CITY_ENG: Optional[str] = None
    DEP_AIRPORT: Optional[str] = None
    DEP_AIRPORT_ENG: Optional[str] = None
    DEP_AIRPORT_CODE: Optional[str] = None
    ARR_AIRPORT: Optional[str] = None
    ARR_AIRPORT_ENG: Optional[str] = None
    ARR_AIRPORT_CODE: Optional[str] = None
    ORIG_FLIGHTID: Optional[str] = None
    ORIG_SEARCHDAY: Optional[str] = None
    RMK_KOR: Optional[str] = None

class FlightStatusArrivalRequest(BaseModel):
    searchday: Optional[str] = None
    from_time: Optional[str] = None
    to_time: Optional[str] = None
    airport_code: Optional[str] = None
    f_id: Optional[str] = None
    flight_id: Optional[str] = None
    line: Optional[str] = None
    serviceKey: Optional[str] = None
    airport: Optional[str] = None
    dep_airport_code: Optional[str] = None
    dep_airport: Optional[str] = None
    fgenTime: Optional[str] = None

class FlightStatusArrivalResponse(BaseModel):
    FGENTIME: Optional[str] = None
    SEARCHDAY: Optional[str] = None
    SCHEDULEDATETIME: Optional[str] = None
    ESTIMATEDDATETIME: Optional[str] = None
    AIRLINE: Optional[str] = None
    CODESHARE: Optional[str] = None
    MASTERFLIGHTID: Optional[str] = None
    FLIGHTID: Optional[str] = None
    LINE: Optional[str] = None
    CITY_ENG: Optional[str] = None
    DEP_AIRPORT: Optional[str] = None
    DEP_AIRPORT_ENG: Optional[str] = None
    DEP_AIRPORT_CODE: Optional[str] = None
    ARR_AIRPORT: Optional[str] = None
    ARR_AIRPORT_ENG: Optional[str] = None
    ARR_AIRPORT_CODE: Optional[str] = None
    ORIG_FLIGHTID: Optional[str] = None
    ORIG_SEARCHDAY: Optional[str] = None
    RMK_KOR: Optional[str] = None

class FlightScheduleTaxfreeDomRequest(BaseModel):
    fid: Optional[str] = None
    flightId: Optional[str] = None
    depCityCode: Optional[str] = None
    depCity: Optional[str] = None
    arrvCityCode: Optional[str] = None
    arrvCity: Optional[str] = None
    serviceKey: Optional[str] = None
    schAirLine: Optional[str] = None
    fgenType: Optional[str] = None
    fgenTime: Optional[str] = None

class FlightScheduleTaxfreeDomResponse(BaseModel):
    fid: Optional[str] = None
    fgenType: Optional[str] = None
    fgenTime: Optional[str] = None
    flightId: Optional[str] = None
    st: Optional[str] = None
    firstdate: Optional[str] = None
    lastdate: Optional[str] = None
    ynMon: Optional[str] = None
    ynTue: Optional[str] = None
    ynWed: Optional[str] = None
    ynThu: Optional[str] = None
    ynFri: Optional[str] = None
    ynSat: Optional[str] = None
    ynSun: Optional[str] = None
    airline: Optional[str] = None
    airlinecode: Optional[str] = None
    depCityCode: Optional[str] = None
    depCity: Optional[str] = None
    arrvCityCode: Optional[str] = None
    arrvCity: Optional[str] = None

class FlightScheduleTaxfreeIntRequest(BaseModel):
    fid: Optional[str] = None
    flightId: Optional[str] = None
    depCityCode: Optional[str] = None
    depCity: Optional[str] = None
    arrvCityCode: Optional[str] = None
    arrvCity: Optional[str] = None
    serviceKey: Optional[str] = None
    schAirLine: Optional[str] = None
    fgenType: Optional[str] = None
    fgenTime: Optional[str] = None

class FlightScheduleTaxfreeIntResponse(BaseModel):
    fid: Optional[str] = None
    fgenType: Optional[str] = None
    fgenTime: Optional[str] = None
    flightId: Optional[str] = None
    st: Optional[str] = None
    firstdate: Optional[str] = None
    lastdate: Optional[str] = None
    ynMon: Optional[str] = None
    ynTue: Optional[str] = None
    ynWed: Optional[str] = None
    ynThu: Optional[str] = None
    ynFri: Optional[str] = None
    ynSat: Optional[str] = None
    ynSun: Optional[str] = None
    airline: Optional[str] = None
    airlinecode: Optional[str] = None
    depCityCode: Optional[str] = None
    depCity: Optional[str] = None
    arrvCityCode: Optional[str] = None
    arrvCity: Optional[str] = None

class ApronCjuRequest(BaseModel):
    FLIGHT_DATE: Optional[str] = None
    STD: Optional[str] = None
    ETD: Optional[str] = None
    LINE: Optional[str] = None
    IO: Optional[str] = None
    AIRPORT: Optional[str] = None
    AIR_FLN: Optional[str] = None

class ApronCjuResponse(BaseModel):
    UFID: Optional[str] = None
    BOARDING_KOR: Optional[str] = None
    BOARDING_ENG: Optional[str] = None
    BOARDING_CHN: Optional[str] = None
    BOARDING_JPN: Optional[str] = None
    ARRIVED_KOR: Optional[str] = None
    ARRIVED_ENG: Optional[str] = None
    ARRIVED_CHN: Optional[str] = None
    ARRIVED_JPN: Optional[str] = None
    AIR_FLN: Optional[str] = None
    FLIGHT_DATE: Optional[str] = None
    LINE: Optional[str] = None
    LINE_CODE: Optional[str] = None
    BAGGAGE_CLAIM: Optional[str] = None
    GATE: Optional[str] = None

class ApronPusRequest(BaseModel):
    flightdate: Optional[str] = None
    std: Optional[str] = None
    etd: Optional[str] = None
    airport: Optional[str] = None
    airfln: Optional[str] = None
    line: Optional[str] = None
    io: Optional[str] = None
    serviceKey: Optional[str] = None

class ApronPusResponse(BaseModel):
    UFID: Optional[str] = None
    BOARDING_KOR: Optional[str] = None
    BOARDING_ENG: Optional[str] = None
    BOARDING_CHN: Optional[str] = None
    BOARDING_JPN: Optional[str] = None
    ARRIVED_KOR: Optional[str] = None
    ARRIVED_ENG: Optional[str] = None
    ARRIVED_CHN: Optional[str] = None
    ARRIVED_JPN: Optional[str] = None
    AIRFLN: Optional[str] = None
    FLIGHTDATE: Optional[str] = None
    LINE: Optional[str] = None
    LINE_CODE: Optional[str] = None
    BAGGAGE_CLAIM: Optional[str] = None
    GATE: Optional[str] = None

class ApronGmpRequest(BaseModel):
    FLIGHT_DATE: Optional[str] = None
    STD: Optional[str] = None
    ETD: Optional[str] = None
    LINE: Optional[str] = None
    IO: Optional[str] = None
    AIRPORT: Optional[str] = None

class ApronGmpResponse(BaseModel):
    UFID: Optional[str] = None
    BOARDING_KOR: Optional[str] = None
    BOARDING_ENG: Optional[str] = None
    BOARDING_CHN: Optional[str] = None
    BOARDING_JPN: Optional[str] = None
    ARRIVED_KOR: Optional[str] = None
    ARRIVED_ENG: Optional[str] = None
    ARRIVED_CHN: Optional[str] = None
    ARRIVED_JPN: Optional[str] = None
    AIR_FLN: Optional[str] = None
    FLIGHT_DATE: Optional[str] = None
    LINE: Optional[str] = None
    LINE_CODE: Optional[str] = None
    BAGGAGE_CLAIM: Optional[str] = None
    GATE: Optional[str] = None

class FlightScheduleDomRequest(BaseModel):
    schDate: Optional[str] = None
    schDeptCityCode: Optional[str] = None
    schArrvCityCode: Optional[str] = None
    schAirLine: Optional[str] = None
    schFlightNum: Optional[str] = None

class FlightScheduleDomResponse(BaseModel):
    STARTCITY_CODE: Optional[str] = None
    STARTCITY: Optional[str] = None
    ARRIVALCITY_CODE: Optional[str] = None
    ARRIVALCITY: Optional[str] = None
    FLIGHT_PURPOSE: Optional[str] = None

class FlightScheduleIntRequest(BaseModel):
    pass

class FlightScheduleIntResponse(BaseModel):
    pass

class FlightStatusDetailRequest(BaseModel):
    pass

class FlightStatusDetailResponse(BaseModel):
    pass

class FlightStatusRequest(BaseModel):
    schStTime: Optional[str] = None
    schEdTime: Optional[str] = None
    schLineType: Optional[str] = None
    schIOType: Optional[str] = None
    schAirCode: Optional[str] = None
    serviceKey: Optional[str] = None
    schFln: Optional[str] = None
    schRmk: Optional[str] = None

class FlightStatusResponse(BaseModel):
    BOARDING_KOR: Optional[str] = None
    BOARDING_ENG: Optional[str] = None
    ARRIVED_KOR: Optional[str] = None
    ARRIVED_ENG: Optional[str] = None
    AIRLINE_KOREAN: Optional[str] = None
    AIRLINE_ENGLISH: Optional[str] = None
    AIR_FLN: Optional[str] = None
    STD: Optional[str] = None
    ETD: Optional[str] = None
    IO: Optional[str] = None
    LINE: Optional[str] = None
    GATE: Optional[str] = None
    RMK_KOR: Optional[str] = None
    RMK_ENG: Optional[str] = None
    CITY: Optional[str] = None
    AIRPORT: Optional[str] = None
