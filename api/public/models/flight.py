from core.models import PublicRequest
from pydantic import BaseModel
from typing import Optional, List, Any

# 기존 API : http://openapi.airport.co.kr/service/rest/statusofPaxSeasonalFlight/getFlightStatusList
# 변경 API : https://apis.airport.co.kr/public/flight/status/taxfree
class FlightStatusTaxfreeRequest(PublicRequest):
    searchDate: Optional[Any] = None
    searchFrom: Optional[Any] = None
    searchTo: Optional[Any] = None
    fid: Optional[Any] = None
    flightId: Optional[Any] = None
    depCityCode: Optional[Any] = None
    depCity: Optional[Any] = None
    arrvCityCode: Optional[Any] = None
    arrvCity: Optional[Any] = None
    fgenType: Optional[Any] = None

class FlightStatusTaxfreeResponse(BaseModel):
    fid: Optional[Any] = None
    fgentime: Optional[Any] = None
    airline: Optional[Any] = None
    arrvairportcode: Optional[Any] = None
    depairport: Optional[Any] = None
    depairportcode: Optional[Any] = None
    arrvairport: Optional[Any] = None
    codeshare: Optional[Any] = None
    masterflightid: Optional[Any] = None
    flightid: Optional[Any] = None
    scheduledatetime: Optional[Any] = None
    estimateddatetime: Optional[Any] = None
    io: Optional[Any] = None
    line: Optional[Any] = None
    fgenType: Optional[Any] = None

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
    fid: Optional[Any] = None
    boardingKor: Optional[Any] = None
    boardingEng: Optional[Any] = None
    city: Optional[Any] = None
    arrivedKor: Optional[Any] = None
    arrivedEng: Optional[Any] = None
    airport: Optional[Any] = None
    airlineKorean: Optional[Any] = None
    airlineEnglish: Optional[Any] = None
    cdsrYn: Optional[Any] = None
    airFln: Optional[Any] = None
    std: Optional[Any] = None
    etd: Optional[Any] = None
    io: Optional[Any] = None
    line: Optional[Any] = None
    rmkKor: Optional[Any] = None
    rmkEng: Optional[Any] = None
    aplRegNo: Optional[Any] = None
    icaoApmCd: Optional[Any] = None
    gate: Optional[Any] = None

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
    airline: Optional[Any] = None
    arrAirport: Optional[Any] = None
    arrAirportEng: Optional[Any] = None
    codeshare: Optional[Any] = None
    depAirport: Optional[Any] = None
    depAirportEng: Optional[Any] = None
    estimateddatetime: Optional[Any] = None
    fid: Optional[Any] = None
    flightid: Optional[Any] = None
    io: Optional[Any] = None
    line: Optional[Any] = None
    masterflightid: Optional[Any] = None
    rmkKor: Optional[Any] = None
    scheduledatetime: Optional[Any] = None
    searchday: Optional[Any] = None
    arrvAirportCode: Optional[Any] = None
    depAirportCode: Optional[Any] = None
    fgenTime: Optional[Any] = None

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
    FID: Optional[Any] = None
    FGENTIME: Optional[Any] = None
    SEARCHDAY: Optional[Any] = None
    SCHEDULEDATETIME: Optional[Any] = None
    ESTIMATEDDATETIME: Optional[Any] = None
    AIRLINE: Optional[Any] = None
    CODESHARE: Optional[Any] = None
    MASTERFLIGHTID: Optional[Any] = None
    FLIGHTID: Optional[Any] = None
    LINE: Optional[Any] = None
    DEP_AIRPORT: Optional[Any] = None
    DEP_AIRPORT_ENG: Optional[Any] = None
    DEP_AIRPORT_CODE: Optional[Any] = None
    ARR_AIRPORT: Optional[Any] = None
    ARR_AIRPORT_ENG: Optional[Any] = None
    ARR_AIRPORT_CODE: Optional[Any] = None
    RMK_KOR: Optional[Any] = None
    IO: Optional[Any] = None

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
    fgentime: Optional[Any] = None
    flightid: Optional[Any] = None
    st: Optional[Any] = None
    firstdate: Optional[Any] = None
    lastdate: Optional[Any] = None
    ynmon: Optional[Any] = None
    yntue: Optional[Any] = None
    ynwed: Optional[Any] = None
    ynthu: Optional[Any] = None
    ynfri: Optional[Any] = None
    ynsat: Optional[Any] = None
    ynsun: Optional[Any] = None
    airline: Optional[Any] = None
    airlineCode: Optional[Any] = None
    depcitycode: Optional[Any] = None
    depcity: Optional[Any] = None
    arrvcitycode: Optional[Any] = None
    arrvcity: Optional[Any] = None

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
    fgentime: Optional[Any] = None
    flightid: Optional[Any] = None
    st: Optional[Any] = None
    firstdate: Optional[Any] = None
    lastdate: Optional[Any] = None
    ynmon: Optional[Any] = None
    yntue: Optional[Any] = None
    ynwed: Optional[Any] = None
    ynthu: Optional[Any] = None
    ynfri: Optional[Any] = None
    ynsat: Optional[Any] = None
    ynsun: Optional[Any] = None
    airline: Optional[Any] = None
    airlinecode: Optional[Any] = None
    depcitycode: Optional[Any] = None
    depcity: Optional[Any] = None
    arrvcitycode: Optional[Any] = None
    arrvcity: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr:80/service/rest/FlightApronStateList/getCJUFlightApronStatusList
# 변경 API : https://apis.airport.co.kr/public/flight/apron-status/cju
class ApronCjuRequest(PublicRequest):
    flightdate: Optional[Any] = None
    std: Optional[Any] = None
    etd: Optional[Any] = None
    line: Optional[Any] = None
    io: Optional[Any] = None
    airport: Optional[Any] = None
    airfln: Optional[Any] = None

class ApronCjuResponse(BaseModel):
    ufid: Optional[Any] = None
    flightDate: Optional[Any] = None
    airFln: Optional[Any] = None
    airlineKorean: Optional[Any] = None
    airlineEnglish: Optional[Any] = None
    boardingKor: Optional[Any] = None
    boardingEng: Optional[Any] = None
    boardingJpn: Optional[Any] = None
    boardingChn: Optional[Any] = None
    arrivedKor: Optional[Any] = None
    arrivedEng: Optional[Any] = None
    arrivedChn: Optional[Any] = None
    arrivedJpn: Optional[Any] = None
    city: Optional[Any] = None
    airport: Optional[Any] = None
    std: Optional[Any] = None
    etd: Optional[Any] = None
    io: Optional[Any] = None
    line: Optional[Any] = None
    lineCode: Optional[Any] = None
    baggageClaim: Optional[Any] = None
    gate: Optional[Any] = None
    rmkKor: Optional[Any] = None
    rmkEng: Optional[Any] = None
    rmkChn: Optional[Any] = None
    rmkJpn: Optional[Any] = None
    sptNm: Optional[Any] = None

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
    ufid: Optional[Any] = None
    flightdate: Optional[Any] = None
    airfln: Optional[Any] = None
    airlineEnglish: Optional[Any] = None
    airlineKorean: Optional[Any] = None
    boardingEng: Optional[Any] = None
    boardingKor: Optional[Any] = None
    boardingJpn: Optional[Any] = None
    boardingChn: Optional[Any] = None
    arrivedEng: Optional[Any] = None
    arrivedKor: Optional[Any] = None
    arrivedChn: Optional[Any] = None
    arrivedJpn: Optional[Any] = None
    city: Optional[Any] = None
    airport: Optional[Any] = None
    std: Optional[Any] = None
    etd: Optional[Any] = None
    io: Optional[Any] = None
    line: Optional[Any] = None
    baggageClaim: Optional[Any] = None
    gate: Optional[Any] = None
    rmkEng: Optional[Any] = None
    rmkKor: Optional[Any] = None
    rmkChn: Optional[Any] = None
    rmkJpn: Optional[Any] = None
    sptNm: Optional[Any] = None
    lineCode: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/FlightApronStateList/getGMPFlightApronStatusList
# 변경 API : https://apis.airport.co.kr/public/flight/apron-status/gmp
class ApronGmpRequest(PublicRequest):
    flightdate: Optional[Any] = None
    std: Optional[Any] = None
    etd: Optional[Any] = None
    airport: Optional[Any] = None
    airfln: Optional[Any] = None
    line: Optional[Any] = None
    io: Optional[Any] = None

class ApronGmpResponse(BaseModel):
    ufid: Optional[Any] = None
    flightDate: Optional[Any] = None
    airFln: Optional[Any] = None
    airlineEnglish: Optional[Any] = None
    airlineKorean: Optional[Any] = None
    boardingEng: Optional[Any] = None
    boardingKor: Optional[Any] = None
    boardingJpn: Optional[Any] = None
    boardingChn: Optional[Any] = None
    arrivedEng: Optional[Any] = None
    arrivedKor: Optional[Any] = None
    arrivedChn: Optional[Any] = None
    arrivedJpn: Optional[Any] = None
    city: Optional[Any] = None
    airport: Optional[Any] = None
    std: Optional[Any] = None
    etd: Optional[Any] = None
    io: Optional[Any] = None
    line: Optional[Any] = None
    lineCode: Optional[Any] = None
    baggageClaim: Optional[Any] = None
    gate: Optional[Any] = None
    rmkEng: Optional[Any] = None
    rmkKor: Optional[Any] = None
    rmkChn: Optional[Any] = None
    rmkJpn: Optional[Any] = None
    sptNm: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/FlightScheduleList/getDflightScheduleList
# 변경 API : https://apis.airport.co.kr/public/flight/schedule/dom
class FlightScheduleDomRequest(PublicRequest):
    schDate: Optional[Any] = None
    schDeptCityCode: Optional[Any] = None
    schArrvCityCode: Optional[Any] = None
    schAirLine: Optional[Any] = None
    schFlightNum: Optional[Any] = None

class FlightScheduleDomResponse(BaseModel):
    airlinehomepageUrl: Optional[Any] = None
    airlineKorean: Optional[Any] = None
    airlineEnglish: Optional[Any] = None
    arrivalcity: Optional[Any] = None
    arrivalcityCode: Optional[Any] = None
    domesticArrivalTime: Optional[Any] = None
    domesticEddate: Optional[Any] = None
    domesticNum: Optional[Any] = None
    domesticStartTime: Optional[Any] = None
    domesticStdate: Optional[Any] = None
    startcity: Optional[Any] = None
    startcityCode: Optional[Any] = None
    domesticSun: Optional[Any] = None
    domesticMon: Optional[Any] = None
    domesticTue: Optional[Any] = None
    domesticWed: Optional[Any] = None
    domesticThu: Optional[Any] = None
    domesticFri: Optional[Any] = None
    domesticSat: Optional[Any] = None
    flightPurpose: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/FlightScheduleList/getIflightScheduleListt
# 변경 API : https://apis.airport.co.kr/public/flight/schedule/int
class FlightScheduleIntRequest(PublicRequest):
    schDate: Optional[Any] = None
    schDeptCityCode: Optional[Any] = None
    schArrvCityCode: Optional[Any] = None
    schAirLine: Optional[Any] = None
    schFlightNum: Optional[Any] = None

class FlightScheduleIntResponse(BaseModel):
    airlinehomepageUrl: Optional[Any] = None
    airlineKorean: Optional[Any] = None
    airlineEnglish: Optional[Any] = None
    airport: Optional[Any] = None
    airportCode: Optional[Any] = None
    city: Optional[Any] = None
    cityCode: Optional[Any] = None
    internationalEddate: Optional[Any] = None
    internationalIoType: Optional[Any] = None
    internationalNum: Optional[Any] = None
    internationalStdate: Optional[Any] = None
    internationalTime: Optional[Any] = None
    internationalSun: Optional[Any] = None
    internationalMon: Optional[Any] = None
    internationalTue: Optional[Any] = None
    internationalWed: Optional[Any] = None
    internationalThu: Optional[Any] = None
    internationalFri: Optional[Any] = None
    internationalSat: Optional[Any] = None
    flightPurpose: Optional[Any] = None

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
    schLineType: Optional[Any] = None
    schIOType: Optional[Any] = None
    schAirCode: Optional[Any] = None
    schStTime: Optional[Any] = None
    schEdTime: Optional[Any] = None

class FlightStatusResponse(BaseModel):
    boardingKor: Optional[Any] = None
    boardingEng: Optional[Any] = None
    arrivedKor: Optional[Any] = None
    arrivedEng: Optional[Any] = None
    airlineKorean: Optional[Any] = None
    airlineEnglish: Optional[Any] = None
    airFln: Optional[Any] = None
    std: Optional[Any] = None
    etd: Optional[Any] = None
    io: Optional[Any] = None
    line: Optional[Any] = None
    gate: Optional[Any] = None
    rmkKor: Optional[Any] = None
    rmkEng: Optional[Any] = None
    city: Optional[Any] = None
    airport: Optional[Any] = None
