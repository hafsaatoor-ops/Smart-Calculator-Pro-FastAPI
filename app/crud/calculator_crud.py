from sqlalchemy.orm import Session

from app.models.history import History
from app.models.user import User


def save_calculation(
    db: Session,
    operation: str,
    number1: float,
    number2: float | None,
    result: float,
    current_user: User
):

    history = History(
        operation=operation,
        number1=number1,
        number2=number2,
        result=result,
        user_id=current_user.id
    )

    db.add(history)

    db.commit()

    db.refresh(history)

    return history