from datetime import date
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.history import History
from app.models.user import User


def get_statistics(
    db: Session,
    current_user: User
):

    total = (
        db.query(History)
        .filter(History.user_id == current_user.id)
        .count()
    )

    average = (
        db.query(func.avg(History.result))
        .filter(History.user_id == current_user.id)
        .scalar()
    )

    today = (
        db.query(History)
        .filter(
            History.user_id == current_user.id,
            func.date(History.created_at) == date.today()
        )
        .count()
    )

    operation = (
        db.query(
            History.operation,
            func.count(History.operation)
        )
        .filter(
            History.user_id == current_user.id
        )
        .group_by(History.operation)
        .order_by(func.count(History.operation).desc())
        .first()
    )

    return {
        "total_calculations": total,
        "most_used_operation": operation[0] if operation else "N/A",
        "average_result": round(average, 2) if average else 0,
        "today_calculations": today
    }