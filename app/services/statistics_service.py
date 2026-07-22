from sqlalchemy.orm import Session

from app.models.history import History
from app.models.user import User


def get_statistics(
    db: Session,
    current_user: User
):

    history = (
        db.query(History)
        .filter(
            History.user_id == current_user.id
        )
        .all()
    )

    total = len(history)

    if total == 0:

        return {
            "total_calculations": 0,
            "average_result": 0,
            "today_calculations": 0,
            "most_used_operation": "-"
        }

    average = sum(
        item.result for item in history
    ) / total

    operations = {}

    for item in history:

        operations[item.operation] = (
            operations.get(item.operation, 0) + 1
        )

    most_used = max(
        operations,
        key=operations.get
    )

    return {

        "total_calculations": total,

        "average_result": average,

        "today_calculations": total,

        "most_used_operation": most_used
    }