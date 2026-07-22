from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.core.dependencies import get_current_user
from app.core.security import create_access_token

from app.models.user import User

from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
)

from app.schemas.token_schema import Token

from app.crud.user_crud import (
    create_user,
    get_user_by_email,
    authenticate_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/signup",
    response_model=UserResponse
)
def signup(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return create_user(db, user)


@router.post(
    "/login",
    response_model=Token
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get(
    "/profile",
    response_model=UserResponse
)
def profile(
    current_user: User = Depends(get_current_user)
):
    return current_user