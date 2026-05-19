from core.models import PublicRequest
from pydantic import BaseModel
from typing import Optional, List, Any

class NoiseStatsRequest(PublicRequest):
    airportCode: Optional[Any] = None
    year: Optional[Any] = None

class NoiseStatsResponse(BaseModel):
    NAME: Optional[Any] = None
    MONTH1: Optional[Any] = None
    MONTH2: Optional[Any] = None
    MONTH3: Optional[Any] = None
    MONTH4: Optional[Any] = None
    MONTH5: Optional[Any] = None
    MONTH6: Optional[Any] = None
    MONTH7: Optional[Any] = None
    MONTH8: Optional[Any] = None
    MONTH9: Optional[Any] = None
    MONTH10: Optional[Any] = None
    MONTH11: Optional[Any] = None
    MONTH12: Optional[Any] = None
    AVERAGE: Optional[Any] = None

class NoiseAffectedAreaRequest(PublicRequest):
    city1: Optional[Any] = None
    city2: Optional[Any] = None
    dong: Optional[Any] = None
    li: Optional[Any] = None
    jibun: Optional[Any] = None
    street: Optional[Any] = None
    build: Optional[Any] = None
    buildno: Optional[Any] = None
    hosu: Optional[Any] = None

class NoiseAffectedAreaResponse(BaseModel):
    CITY1: Optional[Any] = None
    CITY2: Optional[Any] = None
    DONG: Optional[Any] = None
    LI: Optional[Any] = None
    JIBUN: Optional[Any] = None
    STREET: Optional[Any] = None
    BUILD: Optional[Any] = None
    BUILDNO: Optional[Any] = None
    HOSU: Optional[Any] = None

class NoiseRealtimeGmpRequest(PublicRequest):
    pass

class NoiseRealtimeGmpResponse(BaseModel):
    ARP_SE: Optional[Any] = None
    NMS_NM: Optional[Any] = None
    NMT_DT: Optional[Any] = None
    NMT_LVL: Optional[Any] = None
    NMT_NO: Optional[Any] = None

class NoiseRealtimePusRequest(PublicRequest):
    pass

class NoiseRealtimePusResponse(BaseModel):
    ARP_SE: Optional[Any] = None
    NMS_NM: Optional[Any] = None
    NMT_DT: Optional[Any] = None
    NMT_LVL: Optional[Any] = None
    NMT_NO: Optional[Any] = None

