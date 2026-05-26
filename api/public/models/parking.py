from core.models import PublicRequest
from pydantic import BaseModel
from typing import Optional, List, Any

# 기존 API : http://openapi.airport.co.kr/service/rest/AirportParking/airportparkingRT
# 변경 API : https://apis.airport.co.kr/public/parking/realtime-status/info
class AirportParkingRequest(PublicRequest):
    schAirportCode: Optional[Any] = None

class AirportParkingResponse(BaseModel):
    parkingGetdate: Optional[Any] = None
    parkingGettime: Optional[Any] = None
    parkingFullSpace: Optional[Any] = None
    aprKor: Optional[Any] = None
    aprEng: Optional[Any] = None
    parkingAirportCodeName: Optional[Any] = None
    parkingIincnt: Optional[Any] = None
    parkingIoutcnt: Optional[Any] = None
    parkingIstay: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/AirportParkingCongestion/airportParkingCongestionRT
# 변경 API : https://apis.airport.co.kr/public/parking/congestion/info
class ParkingCongestionRequest(PublicRequest):
    schAirportCode: Optional[Any] = None

class ParkingCongestionResponse(BaseModel):
    airportKor: Optional[Any] = None
    airportEng: Optional[Any] = None
    parkingAirportCodeName: Optional[Any] = None
    parkingCongestionDegree: Optional[Any] = None
    parkingCongestion: Optional[Any] = None
    parkingOccupiedSpace: Optional[Any] = None
    parkingTotalSpace: Optional[Any] = None
    sysGetdate: Optional[Any] = None
    sysGettime: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/ValetParking/getGmpDValetParking
# 변경 API : https://apis.airport.co.kr/public/parking/valet-congestion/gmp-dom
class ValetCongestionGmpDomRequest(PublicRequest):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

class ValetCongestionGmpDomResponse(BaseModel):
    crtDt: Optional[Any] = None
    crtTime: Optional[Any] = None
    cam1: Optional[Any] = None
    cam2: Optional[Any] = None
    cam3: Optional[Any] = None
    total: Optional[Any] = None
    cdgr: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/AirportParkingFee/parkingfee
# 변경 API : https://apis.airport.co.kr/public/parking/fee/info
class ParkingFeeRequest(PublicRequest):
    schAirportCode: Optional[Any] = None

class ParkingFeeResponse(BaseModel):
    SITE_NAME: Optional[Any] = None
    PARKING_PARKING_NAME: Optional[Any] = None
    PARKING_BASIC_M: Optional[Any] = None
    PARKING_BASIC_ACCOUNT: Optional[Any] = None
    PARKING_MINUTE_M: Optional[Any] = None
    PARKING_MINUTE_ACCOUNT: Optional[Any] = None
    PARKING_MAX_ACCOUNT: Optional[Any] = None
    PARKING_FREE_M: Optional[Any] = None
    PARKING_CAL_TIME_M: Optional[Any] = None
    PARKING_HOLI_BASIC_M: Optional[Any] = None
    PARKING_HOLI_BASIC_ACCOUNT: Optional[Any] = None
    PARKING_HOLI_MINUTE_M: Optional[Any] = None
    PARKING_HOLI_MINUTE_ACCOUNT: Optional[Any] = None
    PARKING_HOLI_MAX_ACCOUNT: Optional[Any] = None
    PARKING_HOLI_FREE_M: Optional[Any] = None
    PARKING_BASIC_MD: Optional[Any] = None
    PARKING_BASIC_ACCOUNTD: Optional[Any] = None
    PARKING_MINUTE_MD: Optional[Any] = None
    PARKING_MINUTE_ACCOUNTD: Optional[Any] = None
    PARKING_MAX_ACCOUNTD: Optional[Any] = None
    PARKING_FREE_MD: Optional[Any] = None
    PARKING_CAL_TIME_MD: Optional[Any] = None
    PARKING_HOLI_BASIC_MD: Optional[Any] = None
    PARKING_HOLI_BASIC_ACCOUNTD: Optional[Any] = None
    PARKING_HOLI_MINUTE_MD: Optional[Any] = None
    PARKING_HOLI_MINUTE_ACCOUNTD: Optional[Any] = None
    PARKING_HOLI_MAX_ACCOUNTD: Optional[Any] = None
    PARKING_HOLI_FREE_MD: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/airportParkingCell/getGMPParkingCell
# 변경 API : https://apis.airport.co.kr/public/parking/available-spaces/gmp-int-indoor
class AvailableSpacesGmpIntIndoorRequest(PublicRequest):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

class AvailableSpacesGmpIntIndoorResponse(BaseModel):
    cellId: Optional[Any] = None
    parkingName: Optional[Any] = None
    levelName: Optional[Any] = None
    cellType: Optional[Any] = None
    cellStatus: Optional[Any] = None
    updDttm: Optional[Any] = None
    cellName: Optional[Any] = None
