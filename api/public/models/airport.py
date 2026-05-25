from core.models import PublicRequest
from pydantic import BaseModel
from typing import Optional, List, Any

# 기존 API : http://openapi.airport.co.kr/service/rest/AirportBusInfo/businfo
# 변경 API : https://apis.airport.co.kr/public/airport/bus/info
class BusRequest(PublicRequest):
    schAirport: Optional[Any] = None

class BusResponse(BaseModel):
    BUS_CATEGORY_KOR_NAME: Optional[Any] = None
    BUS_DATA_GETON_KOR: Optional[Any] = None
    BUS_DATA_BUS_NUM: Optional[Any] = None
    BUS_DATA_MONEY: Optional[Any] = None
    BUS_DATA_CARD: Optional[Any] = None
    BUS_DATA_ROUTE_KOR: Optional[Any] = None
    BUS_DATA_FIRST_TIME: Optional[Any] = None
    BUS_DATA_END_TIME: Optional[Any] = None
    BUS_DATA_COMNAME_KOR: Optional[Any] = None
    BUS_DATA_ETC_KOR: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/dailyExpectPassenger/dailyExpectPassenger
# 변경 API : https://apis.airport.co.kr/public/airport/daily-expect-passenger/info
class DailyExpectPassengerRequest(PublicRequest):
    schDate: Optional[Any] = None
    schAirport: Optional[Any] = None
    schTof: Optional[Any] = None
    schHH: Optional[Any] = None
    schAOD: Optional[Any] = None

class DailyExpectPassengerResponse(BaseModel):
    TOF: Optional[Any] = None
    CONGEST_YN: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/totalAirportStatsService/getAirportStats
# 변경 API : https://apis.airport.co.kr/public/airport/transport-stats/info
class TransportStatsRequest(PublicRequest):
    startDePd: Optional[Any] = None
    endDePd: Optional[Any] = None
    routeBe: Optional[Any] = None
    nvgBe: Optional[Any] = None
    pasngrCargoBe: Optional[Any] = None
    pasngrBe: Optional[Any] = None
    cargoBe: Optional[Any] = None
    airPort: Optional[Any] = None

class TransportStatsResponse(BaseModel):
    AIRPORT: Optional[Any] = None
    ArrFlgt: Optional[Any] = None
    DepFlgt: Optional[Any] = None
    SubFlgt: Optional[Any] = None
    ArrPassenger: Optional[Any] = None
    DepPassenger: Optional[Any] = None
    SubPassenger: Optional[Any] = None
    ArrCargo: Optional[Any] = None
    DepCargo: Optional[Any] = None
    TotalCargo: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/taxiWaitInfo/getJejuTaxiWaitInfo
# 변경 API : https://apis.airport.co.kr/public/airport/taxi-wait/cju
class TaxiWaitCjuRequest(PublicRequest):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

class TaxiWaitCjuResponse(BaseModel):
    prcdtm: Optional[Any] = None
    wit_Taxi_C_T: Optional[Any] = None
    wit_Pax_C_T: Optional[Any] = None
    xpt_Bdg_Mi: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/AirportLeaseInfo/airportLeaseContract
# 변경 API : https://apis.airport.co.kr/public/airport/lease-contract/info
class LeaseContractRequest(PublicRequest):
    schAirportCode: Optional[Any] = None
    contactStatus: Optional[Any] = None

class LeaseContractResponse(BaseModel):
    STORE_NAME: Optional[Any] = None
    AIRPORT_CODE: Optional[Any] = None
    AIRPORT_NAME: Optional[Any] = None
    LEASE_LOCATION: Optional[Any] = None
    TYPE_OF_BUSINESS: Optional[Any] = None
    SPACE: Optional[Any] = None
    RENTAL: Optional[Any] = None
    CONTRACT_START_DATE: Optional[Any] = None
    CONTRACT_END_DATE: Optional[Any] = None
    CONTRACT_STATUS: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/AirportCodeList/getAirportCodeList
# 변경 API : https://apis.airport.co.kr/public/airport/code/info
class AirportCodeRequest(PublicRequest):
    cityCode: Optional[Any] = None
    cityKor: Optional[Any] = None
    cityEng: Optional[Any] = None
    cityJpn: Optional[Any] = None
    cityChn: Optional[Any] = None

class AirportCodeResponse(BaseModel):
    CITY_CODE: Optional[Any] = None
    CITY_KOR: Optional[Any] = None
    CITY_ENG: Optional[Any] = None
    CITY_JPN: Optional[Any] = None
    CITY_CHN: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/airportLowVisibility/getAirportLowVisibilityIdx
# 변경 API : https://apis.airport.co.kr/public/airport/low-visibility/idx
class LowVisibilityIdxRequest(PublicRequest):
    idx: Optional[Any] = None

class LowVisibilityIdxResponse(BaseModel):
    IDX: Optional[Any] = None
    MTP: Optional[Any] = None
    MEN: Optional[Any] = None
    FRST_REG_TS: Optional[Any] = None
    REG_DATE: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/EpiDataService/getEpiGhDataService
# 변경 API : https://apis.airport.co.kr/public/airport/epi-gh/info
class EpiGhRequest(PublicRequest):
    sdate: Optional[Any] = None
    edate: Optional[Any] = None

class EpiGhResponse(BaseModel):
    YYYY: Optional[Any] = None
    GAS: Optional[Any] = None
    LIQUID: Optional[Any] = None
    CAR: Optional[Any] = None
    SF6: Optional[Any] = None
    SEWAGE: Optional[Any] = None
    ELEC: Optional[Any] = None
    SCOPE3_1: Optional[Any] = None
    SCOPE3_2: Optional[Any] = None
    STEAM1: Optional[Any] = None
    STEAM2: Optional[Any] = None
    DEGU: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/airportLowVisibility/getAirportLowVisibilityLast
# 변경 API : https://apis.airport.co.kr/public/airport/low-visibility/latest
class LowVisibilityLatestRequest(PublicRequest):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

class LowVisibilityLatestResponse(BaseModel):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

# 기존 API : http://openapi.airport.co.kr/service/rest/airportLowVisibility/getAirportLowVisibility
# 변경 API : https://apis.airport.co.kr/public/airport/low-visibility/info
class LowVisibilityRequest(PublicRequest):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

class LowVisibilityResponse(BaseModel):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

# 기존 API : http://openapi.airport.co.kr/service/rest/contractService/getContractNo
# 변경 API : https://apis.airport.co.kr/public/airport/retail-contract/info
class RetailContractRequest(PublicRequest):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

class RetailContractResponse(BaseModel):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

# 기존 API : https://api.odcloud.kr/api/getAPRTPsgrCongestion/v1/aprtPsgrCongestion
# 변경 API : https://apis.airport.co.kr/public/airport/congestion/v1
class CongestionV1Request(PublicRequest):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

class CongestionV1Response(BaseModel):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

# 기존 API : https://api.odcloud.kr/api/getAPRTPsgrCongestion_v2/v1/aprtPsgrCongestionV2
# 변경 API : https://apis.airport.co.kr/public/airport/congestion/v2
class CongestionV2Request(PublicRequest):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

class CongestionV2Response(BaseModel):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

# 기존 API : http://openapi.airport.co.kr/service/rest/jejuOutStats/getJejuOutCntMonth
# 변경 API : https://apis.airport.co.kr/public/airport/montly-inout/cju
class MonthlyInoutCjuRequest(PublicRequest):
    flightDate: Optional[Any] = None
    line: Optional[Any] = None

class MonthlyInoutCjuResponse(BaseModel):
    YM: Optional[Any] = None
    LINE: Optional[Any] = None
    JEJUOUT: Optional[Any] = None

# 기존 API : https://api.odcloud.kr/api/getAPRTWaitTime/v1/aprtWaitTime
# 변경 API : https://apis.airport.co.kr/public/airport/process-time/v1
class ProcessTimeV1Request(PublicRequest):
    pass

class ProcessTimeV1Response(BaseModel):
    IATA_APCD: Optional[Any] = None
    OPR_STS_CD: Optional[Any] = None
    PRC_HR: Optional[Any] = None
    STY_TCT_AVG_A: Optional[Any] = None
    STY_TCT_AVG_ALL: Optional[Any] = None
    STY_TCT_AVG_B: Optional[Any] = None
    STY_TCT_AVG_C: Optional[Any] = None
    STY_TCT_AVG_D: Optional[Any] = None

# 기존 API : https://api.odcloud.kr/api/getAPRTWaitTime_v2/v1/aprtWaitTimeV2
# 변경 API : https://apis.airport.co.kr/public/airport/process-time/v2
class ProcessTimeV2Request(PublicRequest):
    pass

class ProcessTimeV2Response(BaseModel):
    IATA_APCD: Optional[Any] = None
    OPR_STS_CD: Optional[Any] = None
    PRC_HR: Optional[Any] = None
    STY_TCT_AVG_A: Optional[Any] = None
    STY_TCT_AVG_ALL: Optional[Any] = None
    STY_TCT_AVG_B: Optional[Any] = None
    STY_TCT_AVG_C: Optional[Any] = None
    STY_TCT_AVG_D: Optional[Any] = None
