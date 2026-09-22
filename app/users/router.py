from fastapi import APIRouter, Depends, Response

from app.users.schemas import SUserAuth, SUserLogin
from app.users.models import Users
from app.users.dependencies import get_current_user
from app.users.dao import UserDAO
from app.users.auth import get_password_hash, authenticate_user, create_access_token

from exceptions import UserIsNotPresentException, UserAlreadyExistsException


router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException()
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        hashed_password=hashed_password
    )


@router.post("/login")
async def login_user(response: Response, user_data: SUserLogin):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise UserIsNotPresentException()
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("todo_access_token", access_token, httponly=True)
    return access_token


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("todo_access_token")
