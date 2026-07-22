from sqlalchemy.orm import Session

from app.models.history import History
from app.models.user import User
from sqlalchemy import or_

def get_history(
    db: Session,
    current_user: User,
    search: str = None,
    page: int = 1,
    limit: int = 10
):

    query = (
        db.query(History)
        .filter(
            History.user_id == current_user.id
        )
    )

    if search:
        query = query.filter(
            History.operation.ilike(f"%{search}%")
        )

    return (
        query
        .order_by(History.created_at.desc())
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )



def delete_history(
    db: Session,
    history_id: int,
    current_user: User
):

    history = (
        db.query(History)
        .filter(
            History.id == history_id,
            History.user_id == current_user.id
        )
        .first()
    )

    if history:

        db.delete(history)

        db.commit()

        return True

    return False