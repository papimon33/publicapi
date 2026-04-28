from pydantic import BaseModel
from typing import Optional, List

class AirportParkingRequest(BaseModel):
    schAirportCode: Optional[str] = None

class AirportParkingResponse(BaseModel):
    PARKING_GETDATE: Optional[str] = None
    PARKING_GETTIME: Optional[str] = None
    PARKING_FULL_SPACE: Optional[int] = None
    APR_KOR: Optional[str] = None
    APR_ENG: Optional[str] = None

class ParkingCongestionRequest(BaseModel):
    schAirportCode: Optional[str] = None

class ParkingCongestionResponse(BaseModel):
    AIRPORT_KOR: Optional[str] = None
    AIRPORT_ENG: Optional[str] = None
    PARKING_CONGESTION_DEGREE: Optional[str] = None
    PARKING_CONGESTION: Optional[str] = None
    PARKING_OCCUPIED_SPACE: Optional[str] = None
    PARKING_TOTAL_SPACE: Optional[str] = None
    SYS_GETDATE: Optional[str] = None
    SYS_GETTIME: Optional[str] = None

class ValetCongestionRequest(BaseModel):
    pass

class ValetCongestionResponse(BaseModel):
    CDGR: Optional[str] = None

class ParkingFeeRequest(BaseModel):
    schAirportCode: Optional[str] = None

class ParkingFeeResponse(BaseModel):
    pass

class ParkingCellGmpRequest(BaseModel):
    pass

class ParkingCellGmpResponse(BaseModel):
    pass

