from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.calculator_schema import (
    CalculationRequest,
    CalculationResponse
)

from app.services.calculator_service import calculate

from app.crud.calculator_crud import save_calculation

router = APIRouter(
    prefix="/calculator",
    tags=["Calculator"]
)


@router.post(
    "/calculate",
    response_model=CalculationResponse
)
def calculator(
    request: CalculationRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    result = calculate(
        request.operation,
        request.number1,
        request.number2
    )

    save_calculation(
        db,
        request.operation,
        request.number1,
        request.number2,
        result,
        current_user
    )

    return {
        "operation": request.operation,
        "number1": request.number1,
        "number2": request.number2,
        "result": result
    }