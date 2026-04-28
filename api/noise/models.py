from pydantic import BaseModel
from typing import Optional, List

class NoiseStatsRequest(BaseModel):
    airportCode: Optional[str] = None
    year: Optional[str] = None

class NoiseStatsResponse(BaseModel):
    NAME: Optional[str] = None
    MONTH1: Optional[str] = None
    MONTH2: Optional[str] = None
    MONTH3: Optional[str] = None
    MONTH4: Optional[str] = None
    MONTH5: Optional[str] = None
    MONTH6: Optional[str] = None
    MONTH7: Optional[str] = None
    MONTH8: Optional[str] = None
    MONTH9: Optional[str] = None
    MONTH10: Optional[str] = None
    MONTH11: Optional[str] = None
    MONTH12: Optional[str] = None
    AVERAGE: Optional[str] = None

class NoiseAffectedAreaRequest(BaseModel):
    city1: Optional[str] = None
    city2: Optional[str] = None
    dong: Optional[str] = None
    li: Optional[str] = None
    jibun: Optional[str] = None
    street: Optional[str] = None
    build: Optional[str] = None
    buildno: Optional[str] = None
    hosu: Optional[str] = None

class NoiseAffectedAreaResponse(BaseModel):
    CITY1: Optional[str] = None
    CITY2: Optional[str] = None
    DONG: Optional[str] = None
    LI: Optional[str] = None
    JIBUN: Optional[str] = None
    STREET: Optional[str] = None
    BUILD: Optional[str] = None
    BUILDNO: Optional[str] = None
    HOSU: Optional[str] = None

class NoiseRealtimeGmpRequest(BaseModel):
    pass

class NoiseRealtimeGmpResponse(BaseModel):
    pass

class NoiseRealtimePusRequest(BaseModel):
    pass

class NoiseRealtimePusResponse(BaseModel):
    pass

