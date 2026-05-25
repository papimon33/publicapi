from core.models import PublicRequest
from pydantic import BaseModel
from typing import Optional, List, Any

# 기존 API : http://openapi.airport.co.kr/service/rest/statusofPaxSeasonalFlight/getFlightStatusList
# 변경 API : https://apis.airport.co.kr/public/flight/status/taxfree
class FlightStatusTaxfreeRequest(PublicRequest):
    schStTime: Optional[Any] = None
    schEdTime: Optional[Any] = None
    schLineType: Optional[Any] = None
    schIOType: Optional[Any] = None
    schAirCode: Optional[Any] = None
    schFln: Optional[Any] = None
    schRmk: Optional[Any] = None

class FlightStatusTaxfreeResponse(BaseModel):
    BOARDING_KOR: Optional[Any] = None
    BOARDING_ENG: Optional[Any] = None
    ARRIVED_KOR: Optional[Any] = None
    ARRIVED_ENG: Optional[Any] = None
    AIR_FLN: Optional[Any] = None
    LINE: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/serviceLine/serviceLines
# 변경 API : https://apis.airport.co.kr/public/flight/routes/info
class RoutesInfoRequest(PublicRequest):
    schStDate: Optional[Any] = None
    schEdDate: Optional[Any] = None
    schLineType: Optional[Any] = None
    schAirport: Optional[Any] = None

class RoutesInfoResponse(BaseModel):
    ARP: Optional[Any] = None
    ODP: Optional[Any] = None
    TOF: Optional[Any] = None
    KM: Optional[Any] = None
    TIME: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/FlightStatusAPLList/getFlightStatusAPLList
# 변경 API : https://apis.airport.co.kr/public/flight/aircraft-status/info
class AircraftStatusRequest(PublicRequest):
    schStTime: Optional[Any] = None
    schEdTime: Optional[Any] = None
    schAirCode: Optional[Any] = None
    schFID: Optional[Any] = None
    schFln: Optional[Any] = None
    Line: Optional[Any] = None
    schAPLno: Optional[Any] = None
    schAPM: Optional[Any] = None

class AircraftStatusResponse(BaseModel):
    FID: Optional[Any] = None
    AIR_FLN: Optional[Any] = None
    AIRLINE_KOREAN: Optional[Any] = None
    AIRLINE_ENGLISH: Optional[Any] = None
    AIRPORT: Optional[Any] = None
    APL_REG_NO: Optional[Any] = None
    ARRIVED_KOR: Optional[Any] = None
    ARRIVED_ENG: Optional[Any] = None
    BOARDING_KOR: Optional[Any] = None
    BOARDING_ENG: Optional[Any] = None
    CDSR_YN: Optional[Any] = None
    CITY: Optional[Any] = None
    ETD: Optional[Any] = None
    ICAO_APM_CD: Optional[Any] = None
    IO: Optional[Any] = None
    LINE: Optional[Any] = None
    RMK_KOR: Optional[Any] = None
    RMK_ENG: Optional[Any] = None
    STD: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/StatusOfFlights/getDepFlightStatusList
# 변경 API : https://apis.airport.co.kr/public/flight/status/depart
class FlightStatusDepartRequest(PublicRequest):
    searchday: Optional[Any] = None
    from_time: Optional[Any] = None
    to_time: Optional[Any] = None
    airport_code: Optional[Any] = None
    f_id: Optional[Any] = None
    flight_id: Optional[Any] = None
    line: Optional[Any] = None
    airport: Optional[Any] = None

    arr_airport_code: Optional[Any] = None
    arr_airport: Optional[Any] = None
    fgenTime: Optional[Any] = None

class FlightStatusDepartResponse(BaseModel):
    FGENTIME: Optional[Any] = None
    SEARCHDAY: Optional[Any] = None
    SCHEDULEDATETIME: Optional[Any] = None
    ESTIMATEDDATETIME: Optional[Any] = None
    AIRLINE: Optional[Any] = None
    CODESHARE: Optional[Any] = None
    MASTERFLIGHTID: Optional[Any] = None
    FLIGHTID: Optional[Any] = None
    LINE: Optional[Any] = None
    CITY_ENG: Optional[Any] = None
    DEP_AIRPORT: Optional[Any] = None
    DEP_AIRPORT_ENG: Optional[Any] = None
    DEP_AIRPORT_CODE: Optional[Any] = None
    ARR_AIRPORT: Optional[Any] = None
    ARR_AIRPORT_ENG: Optional[Any] = None
    ARR_AIRPORT_CODE: Optional[Any] = None
    ORIG_FLIGHTID: Optional[Any] = None
    ORIG_SEARCHDAY: Optional[Any] = None
    RMK_KOR: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/StatusOfFlights/getArrFlightStatusList
# 변경 API : https://apis.airport.co.kr/public/flight/status/arrival
class FlightStatusArrivalRequest(PublicRequest):
    searchday: Optional[Any] = None
    from_time: Optional[Any] = None
    to_time: Optional[Any] = None
    airport_code: Optional[Any] = None
    f_id: Optional[Any] = None
    flight_id: Optional[Any] = None
    line: Optional[Any] = None
    airport: Optional[Any] = None

    dep_airport_code: Optional[Any] = None
    dep_airport: Optional[Any] = None
    fgenTime: Optional[Any] = None

class FlightStatusArrivalResponse(BaseModel):
    FGENTIME: Optional[Any] = None
    SEARCHDAY: Optional[Any] = None
    SCHEDULEDATETIME: Optional[Any] = None
    ESTIMATEDDATETIME: Optional[Any] = None
    AIRLINE: Optional[Any] = None
    CODESHARE: Optional[Any] = None
    MASTERFLIGHTID: Optional[Any] = None
    FLIGHTID: Optional[Any] = None
    LINE: Optional[Any] = None
    CITY_ENG: Optional[Any] = None
    DEP_AIRPORT: Optional[Any] = None
    DEP_AIRPORT_ENG: Optional[Any] = None
    DEP_AIRPORT_CODE: Optional[Any] = None
    ARR_AIRPORT: Optional[Any] = None
    ARR_AIRPORT_ENG: Optional[Any] = None
    ARR_AIRPORT_CODE: Optional[Any] = None
    ORIG_FLIGHTID: Optional[Any] = None
    ORIG_SEARCHDAY: Optional[Any] = None
    RMK_KOR: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/statusofPaxSeasonalFlight/getDPaxSfitSched
# 변경 API : https://apis.airport.co.kr/public/flight/schedule/taxfree-dom
class FlightScheduleTaxfreeDomRequest(PublicRequest):
    fid: Optional[Any] = None
    flightId: Optional[Any] = None
    depCityCode: Optional[Any] = None
    depCity: Optional[Any] = None
    arrvCityCode: Optional[Any] = None
    arrvCity: Optional[Any] = None
    schAirLine: Optional[Any] = None

    fgenType: Optional[Any] = None
    fgenTime: Optional[Any] = None

class FlightScheduleTaxfreeDomResponse(BaseModel):
    fid: Optional[Any] = None
    fgenType: Optional[Any] = None
    fgenTime: Optional[Any] = None
    flightId: Optional[Any] = None
    st: Optional[Any] = None
    firstdate: Optional[Any] = None
    lastdate: Optional[Any] = None
    ynMon: Optional[Any] = None
    ynTue: Optional[Any] = None
    ynWed: Optional[Any] = None
    ynThu: Optional[Any] = None
    ynFri: Optional[Any] = None
    ynSat: Optional[Any] = None
    ynSun: Optional[Any] = None
    airline: Optional[Any] = None
    airlinecode: Optional[Any] = None
    depCityCode: Optional[Any] = None
    depCity: Optional[Any] = None
    arrvCityCode: Optional[Any] = None
    arrvCity: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/statusofPaxSeasonalFlight/getIPaxSfitSched
# 변경 API : https://apis.airport.co.kr/public/flight/schedule/taxfree-int
class FlightScheduleTaxfreeIntRequest(PublicRequest):
    fid: Optional[Any] = None
    flightId: Optional[Any] = None
    depCityCode: Optional[Any] = None
    depCity: Optional[Any] = None
    arrvCityCode: Optional[Any] = None
    arrvCity: Optional[Any] = None
    schAirLine: Optional[Any] = None

    fgenType: Optional[Any] = None
    fgenTime: Optional[Any] = None

class FlightScheduleTaxfreeIntResponse(BaseModel):
    fid: Optional[Any] = None
    fgenType: Optional[Any] = None
    fgenTime: Optional[Any] = None
    flightId: Optional[Any] = None
    st: Optional[Any] = None
    firstdate: Optional[Any] = None
    lastdate: Optional[Any] = None
    ynMon: Optional[Any] = None
    ynTue: Optional[Any] = None
    ynWed: Optional[Any] = None
    ynThu: Optional[Any] = None
    ynFri: Optional[Any] = None
    ynSat: Optional[Any] = None
    ynSun: Optional[Any] = None
    airline: Optional[Any] = None
    airlinecode: Optional[Any] = None
    depCityCode: Optional[Any] = None
    depCity: Optional[Any] = None
    arrvCityCode: Optional[Any] = None
    arrvCity: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr:80/service/rest/FlightApronStateList/getCJUFlightApronStatusList
# 변경 API : https://apis.airport.co.kr/public/flight/apron-status/cju
class ApronCjuRequest(PublicRequest):
    FLIGHT_DATE: Optional[Any] = None
    STD: Optional[Any] = None
    ETD: Optional[Any] = None
    LINE: Optional[Any] = None
    IO: Optional[Any] = None
    AIRPORT: Optional[Any] = None
    AIR_FLN: Optional[Any] = None

class ApronCjuResponse(BaseModel):
    UFID: Optional[Any] = None
    BOARDING_KOR: Optional[Any] = None
    BOARDING_ENG: Optional[Any] = None
    BOARDING_CHN: Optional[Any] = None
    BOARDING_JPN: Optional[Any] = None
    ARRIVED_KOR: Optional[Any] = None
    ARRIVED_ENG: Optional[Any] = None
    ARRIVED_CHN: Optional[Any] = None
    ARRIVED_JPN: Optional[Any] = None
    AIR_FLN: Optional[Any] = None
    FLIGHT_DATE: Optional[Any] = None
    LINE: Optional[Any] = None
    LINE_CODE: Optional[Any] = None
    BAGGAGE_CLAIM: Optional[Any] = None
    GATE: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/FlightApronStateList/getFlightApronStatusList
# 변경 API : https://apis.airport.co.kr/public/flight/apron-status/pus
class ApronPusRequest(PublicRequest):
    flightdate: Optional[Any] = None
    std: Optional[Any] = None
    etd: Optional[Any] = None
    airport: Optional[Any] = None
    airfln: Optional[Any] = None
    line: Optional[Any] = None
    io: Optional[Any] = None

class ApronPusResponse(BaseModel):
    UFID: Optional[Any] = None
    BOARDING_KOR: Optional[Any] = None
    BOARDING_ENG: Optional[Any] = None
    BOARDING_CHN: Optional[Any] = None
    BOARDING_JPN: Optional[Any] = None
    ARRIVED_KOR: Optional[Any] = None
    ARRIVED_ENG: Optional[Any] = None
    ARRIVED_CHN: Optional[Any] = None
    ARRIVED_JPN: Optional[Any] = None
    AIRFLN: Optional[Any] = None
    FLIGHTDATE: Optional[Any] = None
    LINE: Optional[Any] = None
    LINE_CODE: Optional[Any] = None
    BAGGAGE_CLAIM: Optional[Any] = None
    GATE: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/FlightApronStateList/getGMPFlightApronStatusList
# 변경 API : https://apis.airport.co.kr/public/flight/apron-status/gmp
class ApronGmpRequest(PublicRequest):
    FLIGHT_DATE: Optional[Any] = None
    STD: Optional[Any] = None
    ETD: Optional[Any] = None
    LINE: Optional[Any] = None
    IO: Optional[Any] = None
    AIRPORT: Optional[Any] = None

class ApronGmpResponse(BaseModel):
    UFID: Optional[Any] = None
    BOARDING_KOR: Optional[Any] = None
    BOARDING_ENG: Optional[Any] = None
    BOARDING_CHN: Optional[Any] = None
    BOARDING_JPN: Optional[Any] = None
    ARRIVED_KOR: Optional[Any] = None
    ARRIVED_ENG: Optional[Any] = None
    ARRIVED_CHN: Optional[Any] = None
    ARRIVED_JPN: Optional[Any] = None
    AIR_FLN: Optional[Any] = None
    FLIGHT_DATE: Optional[Any] = None
    LINE: Optional[Any] = None
    LINE_CODE: Optional[Any] = None
    BAGGAGE_CLAIM: Optional[Any] = None
    GATE: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/FlightScheduleList/getDflightScheduleList
# 변경 API : https://apis.airport.co.kr/public/flight/schedule/dom
class FlightScheduleDomRequest(PublicRequest):
    schDate: Optional[Any] = None
    schDeptCityCode: Optional[Any] = None
    schArrvCityCode: Optional[Any] = None
    schAirLine: Optional[Any] = None
    schFlightNum: Optional[Any] = None

class FlightScheduleDomResponse(BaseModel):
    STARTCITY_CODE: Optional[Any] = None
    STARTCITY: Optional[Any] = None
    ARRIVALCITY_CODE: Optional[Any] = None
    ARRIVALCITY: Optional[Any] = None
    FLIGHT_PURPOSE: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/FlightScheduleList/getIflightScheduleListt
# 변경 API : https://apis.airport.co.kr/public/flight/schedule/int
class FlightScheduleIntRequest(PublicRequest):
    schDate: Optional[Any] = None
    schDeptCityCode: Optional[Any] = None
    schArrvCityCode: Optional[Any] = None
    schAirLine: Optional[Any] = None
    schFlightNum: Optional[Any] = None

class FlightScheduleIntResponse(BaseModel):
    INTERNATIONAL_IO_TYPE: Optional[Any] = None
    INTERNATIONAL_NUM: Optional[Any] = None
    INTERNATIONAL_TIME: Optional[Any] = None
    INTERNATIONAL_MON: Optional[Any] = None
    INTERNATIONAL_TUE: Optional[Any] = None
    INTERNATIONAL_WED: Optional[Any] = None
    INTERNATIONAL_THU: Optional[Any] = None
    INTERNATIONAL_FRI: Optional[Any] = None
    INTERNATIONAL_SAT: Optional[Any] = None
    INTERNATIONAL_SUN: Optional[Any] = None
    INTERNATIONAL_STDATE: Optional[Any] = None
    INTERNATIONAL_EDDATE: Optional[Any] = None
    AIRLINE_KOREAN: Optional[Any] = None
    AIRLINE_ENGLISH: Optional[Any] = None
    AIRLINE_HOMEPAGE_URL: Optional[Any] = None
    AIRPORT_CODE: Optional[Any] = None
    AIRPORT: Optional[Any] = None
    CITY_CODE: Optional[Any] = None
    CITY: Optional[Any] = None
    FLIGHT_PURPOSE: Optional[Any] = None

# 기존 API : https://api.odcloud.kr/api/FlightStatusListDTL/v1/getFlightStatusListDetail
# 변경 API : https://apis.airport.co.kr/public/flight/status/detail
class FlightStatusDetailRequest(PublicRequest):
    pass

class FlightStatusDetailResponse(BaseModel):
    UFID: Optional[Any] = None
    AIRLINE_KOREAN: Optional[Any] = None
    AIRLINE_ENGLISH: Optional[Any] = None
    AIRPORT: Optional[Any] = None
    AIR_FLN: Optional[Any] = None
    BOARDING_KOR: Optional[Any] = None
    BOARDING_ENG: Optional[Any] = None
    ARRIVED_KOR: Optional[Any] = None
    ARRIVED_ENG: Optional[Any] = None
    CITY: Optional[Any] = None
    STD: Optional[Any] = None
    ETD: Optional[Any] = None
    FLIGHT_DATE: Optional[Any] = None
    IO: Optional[Any] = None
    LINE: Optional[Any] = None
    LINE_CODE: Optional[Any] = None
    GATE: Optional[Any] = None
    BAGGAGE_CLAIM: Optional[Any] = None
    RMK_KOR: Optional[Any] = None
    RMK_ENG: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList
# 변경 API : https://apis.airport.co.kr/public/flight/status/info
class FlightStatusRequest(PublicRequest):
    schStTime: Optional[Any] = None
    schEdTime: Optional[Any] = None
    schLineType: Optional[Any] = None
    schIOType: Optional[Any] = None
    schAirCode: Optional[Any] = None
    schFln: Optional[Any] = None
    schRmk: Optional[Any] = None

class FlightStatusResponse(BaseModel):
    BOARDING_KOR: Optional[Any] = None
    BOARDING_ENG: Optional[Any] = None
    ARRIVED_KOR: Optional[Any] = None
    ARRIVED_ENG: Optional[Any] = None
    AIRLINE_KOREAN: Optional[Any] = None
    AIRLINE_ENGLISH: Optional[Any] = None
    AIR_FLN: Optional[Any] = None
    STD: Optional[Any] = None
    ETD: Optional[Any] = None
    IO: Optional[Any] = None
    LINE: Optional[Any] = None
    GATE: Optional[Any] = None
    RMK_KOR: Optional[Any] = None
    RMK_ENG: Optional[Any] = None
    CITY: Optional[Any] = None
    AIRPORT: Optional[Any] = None
