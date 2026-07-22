from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from app.database.session import get_db
from fastapi import Query
from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.history_schema import HistoryResponse

from app.crud.history_crud import (
    get_history,
    delete_history
)

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get(
    "/",
    response_model=list[HistoryResponse]
)
def history(

    search: Optional[str] = None,

    page: int = Query(1, ge=1),

    limit: int = Query(10, ge=1, le=100),

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    return get_history(
        db=db,
        current_user=current_user,
        search=search,
        page=page,
        limit=limit
    )


@router.delete("/{history_id}")
def delete(
    history_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    deleted = delete_history(
        db,
        history_id,
        current_user
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="History not found"
        )

    return {
        "message": "History deleted successfully"
    }