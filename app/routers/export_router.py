from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.core.dependencies import get_current_user

from app.models.user import User
from app.models.history import History

from app.utils.export import create_csv

router = APIRouter(
    prefix="/export",
    tags=["Export"]
)


@router.get("/")
def export_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    history = (
        db.query(History)
        .filter(History.user_id == current_user.id)
        .all()
    )

    csv_file = create_csv(history)

    return StreamingResponse(
        iter([csv_file.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=history.csv"
        }
    )