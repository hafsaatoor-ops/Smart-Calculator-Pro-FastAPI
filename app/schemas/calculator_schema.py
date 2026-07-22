from pydantic import BaseModel


class CalculationRequest(BaseModel):
    operation: str
    number1: float
    number2: float | None = None


class CalculationResponse(BaseModel):
    operation: str
    number1: float
    number2: float | None = None
    result: float