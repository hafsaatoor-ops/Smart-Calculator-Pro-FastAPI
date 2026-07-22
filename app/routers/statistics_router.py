from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.statistics_schema import StatisticsResponse

from app.crud.statistics_crud import get_statistics

router = APIRouter(
    prefix="/statistics",
    tags=["Statistics"]
)


@router.get(
    "/",
    response_model=StatisticsResponse
)
def statistics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_statistics(
        db,
        current_user
    )