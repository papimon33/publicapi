from core.models import PublicRequest
from pydantic import BaseModel
from typing import Optional, List, Any

# 기존 API : http://openapi.airport.co.kr/service/rest/AirportParking/airportparkingRT
# 변경 API : https://apis.airport.co.kr/public/parking/realtime-status/info
class AirportParkingRequest(PublicRequest):
    schAirportCode: Optional[Any] = None

class AirportParkingResponse(BaseModel):
    PARKING_GETDATE: Optional[Any] = None
    PARKING_GETTIME: Optional[Any] = None
    PARKING_FULL_SPACE: Optional[Any] = None
    APR_KOR: Optional[Any] = None
    APR_ENG: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/AirportParkingCongestion/airportParkingCongestionRT
# 변경 API : https://apis.airport.co.kr/public/parking/congestion/info
class ParkingCongestionRequest(PublicRequest):
    schAirportCode: Optional[Any] = None

class ParkingCongestionResponse(BaseModel):
    AIRPORT_KOR: Optional[Any] = None
    AIRPORT_ENG: Optional[Any] = None
    PARKING_CONGESTION_DEGREE: Optional[Any] = None
    PARKING_CONGESTION: Optional[Any] = None
    PARKING_OCCUPIED_SPACE: Optional[Any] = None
    PARKING_TOTAL_SPACE: Optional[Any] = None
    SYS_GETDATE: Optional[Any] = None
    SYS_GETTIME: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/ValetParking/getGmpDValetParking
# 변경 API : https://apis.airport.co.kr/public/parking/valet-congestion/gmp-dom
class ValetCongestionGmpDomRequest(PublicRequest):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

class ValetCongestionGmpDomResponse(BaseModel):
    CDGR: Optional[Any] = None

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
    # 모델에 대응하는 SQL을 찾지 못함
    pass
