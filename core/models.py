from pydantic import BaseModel, Field
from typing import TypeVar, Generic, List, Optional

T = TypeVar("T")

class PublicRequest(BaseModel):
    type: Optional[str] = Field(default="json", description="응답 형식 (xml/json)")

class PaginationParams(BaseModel):
    numOfRows: int = Field(default=10, ge=1, le=100, description="한 페이지 결과 수 (최대 100)")
    pageNo: int = Field(default=1, ge=1, description="페이지 번호")

class ResponseHeader(BaseModel):
    resultCode: str = Field(default="00")
    resultMessage: str = Field(default="NORMAL SERVICE.")

class PaginationResponseBody(BaseModel, Generic[T]):
    data: List[T]
    numOfRows: int
    pageNo: int
    totalCount: int

class PaginationResponse(BaseModel, Generic[T]):
    header: ResponseHeader = Field(default_factory=ResponseHeader)
    body: PaginationResponseBody[T]
