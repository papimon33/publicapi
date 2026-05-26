from core.models import PublicRequest
from pydantic import BaseModel
from typing import Optional, List, Any

# 기존 API : http://openapi.airport.co.kr/service/rest/noiseMeasureService/getNoiseMeasure
# 변경 API : https://apis.airport.co.kr/public/noise/measure/info
class NoiseStatsRequest(PublicRequest):
    airportCode: Optional[Any] = None
    year: Optional[Any] = None

class NoiseStatsResponse(BaseModel):
    name: Optional[Any] = None
    month1: Optional[Any] = None
    month2: Optional[Any] = None
    month3: Optional[Any] = None
    month4: Optional[Any] = None
    month5: Optional[Any] = None
    month6: Optional[Any] = None
    month7: Optional[Any] = None
    month8: Optional[Any] = None
    month9: Optional[Any] = None
    month10: Optional[Any] = None
    month11: Optional[Any] = None
    month12: Optional[Any] = None
    average: Optional[Any] = None

# 기존 API : http://openapi.airport.co.kr/service/rest/noise/noiseAffectedArea
# 변경 API : https://apis.airport.co.kr/public/noise/affected-area/info
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
    city1: Optional[Any] = None
    city2: Optional[Any] = None
    dong: Optional[Any] = None
    li: Optional[Any] = None
    jibun: Optional[Any] = None
    street: Optional[Any] = None
    build: Optional[Any] = None
    buildno: Optional[Any] = None
    hosu: Optional[Any] = None
    yn: Optional[Any] = None

# 기존 API : https://api.odcloud.kr/api/getNoiseMeasureRT/v1/noiseMeasureRT
# 변경 API : https://apis.airport.co.kr/public/noise/realtime-measure/gmp
class NoiseRealtimeGmpRequest(PublicRequest):
    pass

class NoiseRealtimeGmpResponse(BaseModel):
    ARP_SE: Optional[Any] = None
    NMS_NM: Optional[Any] = None
    NMT_DT: Optional[Any] = None
    NMT_LVL: Optional[Any] = None
    NMT_NO: Optional[Any] = None

# 기존 API : https://api.odcloud.kr/api/getNoiseMeasurePUS/v1/noiseMeasurePUS
# 변경 API : https://apis.airport.co.kr/public/noise/realtime-measure/pus
class NoiseRealtimePusRequest(PublicRequest):
    pass

class NoiseRealtimePusResponse(BaseModel):
    ARP_SE: Optional[Any] = None
    NMS_NM: Optional[Any] = None
    NMT_DT: Optional[Any] = None
    NMT_LVL: Optional[Any] = None
    NMT_NO: Optional[Any] = None
