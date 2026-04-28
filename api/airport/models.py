from pydantic import BaseModel
from typing import Optional, List

class BusRequest(BaseModel):
    schAirport: Optional[str] = None

class BusResponse(BaseModel):
    BUS_CATEGORY_KOR_NAME: Optional[str] = None
    BUS_DATA_GETON_KOR: Optional[str] = None
    BUS_DATA_BUS_NUM: Optional[str] = None
    BUS_DATA_MONEY: Optional[str] = None
    BUS_DATA_CARD: Optional[str] = None
    BUS_DATA_ROUTE_KOR: Optional[str] = None
    BUS_DATA_FIRST_TIME: Optional[str] = None
    BUS_DATA_END_TIME: Optional[str] = None
    BUS_DATA_COMNAME_KOR: Optional[str] = None
    BUS_DATA_ETC_KOR: Optional[str] = None

class DailyExpectPassengerRequest(BaseModel):
    schDate: Optional[str] = None
    schAirport: Optional[str] = None
    schTof: Optional[str] = None
    schHH: Optional[str] = None
    serviceKey: Optional[str] = None
    schAOD: Optional[str] = None

class DailyExpectPassengerResponse(BaseModel):
    TOF: Optional[str] = None
    CONGEST_YN: Optional[str] = None

class TransportStatsRequest(BaseModel):
    startDePd: Optional[str] = None
    endDePd: Optional[str] = None
    routeBe: Optional[str] = None
    nvgBe: Optional[str] = None
    pasngrCargoBe: Optional[str] = None
    pasngrBe: Optional[str] = None
    cargoBe: Optional[str] = None
    airPort: Optional[str] = None

class TransportStatsResponse(BaseModel):
    pass

class TaxiWaitCjuRequest(BaseModel):
    pass

class TaxiWaitCjuResponse(BaseModel):
    prcdtm: Optional[str] = None
    wit_Taxi_C_T: Optional[str] = None
    wit_Pax_C_T: Optional[str] = None
    xpt_Bdg_Mi: Optional[str] = None

class LeaseContractRequest(BaseModel):
    schAirportCode: Optional[str] = None
    contactStatus: Optional[str] = None

class LeaseContractResponse(BaseModel):
    STORE_NAME: Optional[str] = None
    AIRPORT_CODE: Optional[str] = None
    AIRPORT_NAME: Optional[str] = None
    LEASE_LOCATION: Optional[str] = None
    TYPE_OF_BUSINESS: Optional[str] = None
    SPACE: Optional[str] = None
    RENTAL: Optional[str] = None
    CONTRACT_START_DATE: Optional[str] = None
    CONTRACT_END_DATE: Optional[str] = None
    CONTRACT_STATUS: Optional[str] = None

class AirportCodeRequest(BaseModel):
    serviceKey: Optional[str] = None
    cityCode: Optional[str] = None
    cityKor: Optional[str] = None
    cityEng: Optional[str] = None
    cityJpn: Optional[str] = None
    cityChn: Optional[str] = None
    numOfRows: Optional[str] = None
    pageNo: Optional[str] = None

class AirportCodeResponse(BaseModel):
    pass

class LowVisibilityIdxRequest(BaseModel):
    idx: Optional[str] = None

class LowVisibilityIdxResponse(BaseModel):
    pass

class EpiGhRequest(BaseModel):
    sdate: Optional[str] = None
    edate: Optional[str] = None

class EpiGhResponse(BaseModel):
    YYYY: Optional[str] = None
    GAS: Optional[str] = None
    LIQUID: Optional[str] = None
    CAR: Optional[str] = None
    SF6: Optional[str] = None
    SEWAGE: Optional[str] = None
    ELEC: Optional[str] = None
    SCOPE3_1: Optional[str] = None
    SCOPE3_2: Optional[str] = None
    STEAM1: Optional[str] = None
    STEAM2: Optional[str] = None
    DEGU: Optional[str] = None

class LowVisibilityLatestRequest(BaseModel):
    pass

class LowVisibilityLatestResponse(BaseModel):
    pass

class LowVisibilityRequest(BaseModel):
    pass

class LowVisibilityResponse(BaseModel):
    pass

class RetailContractRequest(BaseModel):
    pass

class RetailContractResponse(BaseModel):
    pass

class CongestionV1Request(BaseModel):
    pass

class CongestionV1Response(BaseModel):
    pass

class CongestionV2Request(BaseModel):
    pass

class CongestionV2Response(BaseModel):
    pass

class MonthlyInoutCjuRequest(BaseModel):
    pass

class MonthlyInoutCjuResponse(BaseModel):
    pass

class WaitTimeV1Request(BaseModel):
    pass

class WaitTimeV1Response(BaseModel):
    pass

class WaitTimeV2Request(BaseModel):
    pass

class WaitTimeV2Response(BaseModel):
    pass

