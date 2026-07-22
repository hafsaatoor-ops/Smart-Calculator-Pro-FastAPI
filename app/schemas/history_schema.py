from pydantic import BaseModel
from datetime import datetime


class HistoryCreate(BaseModel):
    operation: str
    number1: float
    number2: float | None = None


class HistoryResponse(BaseModel):
    id: int
    operation: str
    number1: float
    number2: float | None
    result: float
    created_at: datetime

    class Config:
        from_attributes = True