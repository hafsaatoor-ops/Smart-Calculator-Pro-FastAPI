from pydantic import BaseModel


class StatisticsResponse(BaseModel):

    total_calculations: int

    most_used_operation: str

    average_result: float

    today_calculations: int