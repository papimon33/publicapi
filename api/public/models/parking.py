from core.models import PublicRequest
from pydantic import BaseModel
from typing import Optional, List, Any

class AirportParkingRequest(PublicRequest):
    schAirportCode: Optional[Any] = None

class AirportParkingResponse(BaseModel):
    PARKING_GETDATE: Optional[Any] = None
    PARKING_GETTIME: Optional[Any] = None
    PARKING_FULL_SPACE: Optional[Any] = None
    APR_KOR: Optional[Any] = None
    APR_ENG: Optional[Any] = None

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

class ValetCongestionRequest(PublicRequest):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

class ValetCongestionResponse(BaseModel):
    CDGR: Optional[Any] = None

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

class ParkingCellGmpRequest(PublicRequest):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

class ParkingCellGmpResponse(BaseModel):
    # 모델에 대응하는 SQL을 찾지 못함
    pass

