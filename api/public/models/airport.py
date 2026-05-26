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

class DailyExpectPassengerResponse(BaseModel):
    ARP: Optional[Any] = None
    AOD: Optional[Any] = None
    SDT: Optional[Any] = None
    HH: Optional[Any] = None
    PCT: Optional[Any] = None
    PCG: Optional[Any] = None
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

class TransportStatsResponse(BaseModel):
    Airport: Optional[Any] = None
    Arrflgt: Optional[Any] = None
    depflgtn: Optional[Any] = None
    Subflgt: Optional[Any] = None
    Arrpassenger: Optional[Any] = None
    Deppassenger: Optional[Any] = None
    subpassenger: Optional[Any] = None
    Arrcargo: Optional[Any] = None
    Depcargo: Optional[Any] = None
    subcargo: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/taxiWaitInfo/getJejuTaxiWaitInfo
# 변경 API : https://apis.airport.co.kr/public/airport/taxi-wait/cju
class TaxiWaitCjuRequest(PublicRequest):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

class TaxiWaitCjuResponse(BaseModel):
    prcdtm: Optional[Any] = None
    witTaxiCT: Optional[Any] = None
    witPaxCT: Optional[Any] = None
    xptBdgMi: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/AirportLeaseInfo/airportLeaseContract
# 변경 API : https://apis.airport.co.kr/public/airport/lease-contract/info
class LeaseContractRequest(PublicRequest):
    schAirportCode: Optional[Any] = None
    contractStatus: Optional[Any] = None

class LeaseContractResponse(BaseModel):
    storeName: Optional[Any] = None
    airportCode: Optional[Any] = None
    airportName: Optional[Any] = None
    leaseLocation: Optional[Any] = None
    typeOfBusiness: Optional[Any] = None
    space: Optional[Any] = None
    rental: Optional[Any] = None
    contractStartDate: Optional[Any] = None
    contractEndDate: Optional[Any] = None
    contractStatus: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/AirportCodeList/getAirportCodeList
# 변경 API : https://apis.airport.co.kr/public/airport/code/info
class AirportCodeRequest(PublicRequest):
    cityCode: Optional[Any] = None
    cityKor: Optional[Any] = None
    cityEng: Optional[Any] = None
    cityJpn: Optional[Any] = None
    cityChn: Optional[Any] = None

class AirportCodeResponse(BaseModel):
    cityCode: Optional[Any] = None
    cityKorean: Optional[Any] = None
    cityEnglish: Optional[Any] = None
    cityJapan: Optional[Any] = None
    cityChina: Optional[Any] = None

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
    gnr: Optional[Any] = None
    str: Optional[Any] = None
    total: Optional[Any] = None
    yyyy: Optional[Any] = None
    fuel1: Optional[Any] = None
    fuel2: Optional[Any] = None
    totalTco2e: Optional[Any] = None
    engUseTj: Optional[Any] = None
    jihasu: Optional[Any] = None
    jungsu: Optional[Any] = None
    sisu: Optional[Any] = None
    fix: Optional[Any] = None

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
    Gtext: Optional[Any] = None
    Name1: Optional[Any] = None
    Sangho: Optional[Any] = None
    ConfDate: Optional[Any] = None
    ContDate: Optional[Any] = None
    Type3Text: Optional[Any] = None
    Type4Text: Optional[Any] = None

# 기존 API : https://api.odcloud.kr/api/getAPRTPsgrCongestion/v1/aprtPsgrCongestion
# 변경 API : https://apis.airport.co.kr/public/airport/congestion/v1
class CongestionV1Request(PublicRequest):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

class CongestionV1Response(BaseModel):
    IATA_APCD: Optional[Any] = None
    PRC_HR: Optional[Any] = None
    CGDR_A_LVL: Optional[Any] = None
    CGDR_B_LVL: Optional[Any] = None
    CGDR_C_LVL: Optional[Any] = None
    CGDR_ALL_LVL: Optional[Any] = None

# 기존 API : https://api.odcloud.kr/api/getAPRTPsgrCongestion_v2/v1/aprtPsgrCongestionV2
# 변경 API : https://apis.airport.co.kr/public/airport/congestion/v2
class CongestionV2Request(PublicRequest):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

class CongestionV2Response(BaseModel):
    IATA_APCD: Optional[Any] = None
    PRC_HR: Optional[Any] = None
    CGDR_A_LVL: Optional[Any] = None
    CGDR_B_LVL: Optional[Any] = None
    CGDR_C_LVL: Optional[Any] = None
    CGDR_ALL_LVL: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/jejuOutStats/getJejuOutCntMonth
# 변경 API : https://apis.airport.co.kr/public/airport/montly-inout/cju
class MonthlyInoutCjuRequest(PublicRequest):
    ym: Optional[Any] = None
    line: Optional[Any] = None

class MonthlyInoutCjuResponse(BaseModel):
    ym: Optional[Any] = None
    line: Optional[Any] = None
    jejuout: Optional[Any] = None

# 기존 API : https://api.odcloud.kr/api/getAPRTWaitTime/v1/aprtWaitTime
# 변경 API : https://apis.airport.co.kr/public/airport/process-time/v1
class ProcessTimeV1Request(PublicRequest):
    IATA_APCD: Optional[Any] = None

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
    IATA_APCD: Optional[Any] = None

class ProcessTimeV2Response(BaseModel):
    IATA_APCD: Optional[Any] = None
    OPR_STS_CD: Optional[Any] = None
    PRC_HR: Optional[Any] = None
    STY_TCT_AVG_A: Optional[Any] = None
    STY_TCT_AVG_ALL: Optional[Any] = None
    STY_TCT_AVG_B: Optional[Any] = None
    STY_TCT_AVG_C: Optional[Any] = None
    STY_TCT_AVG_D: Optional[Any] = None
