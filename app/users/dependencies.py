from fastapi import Request, Depends
from jose import jwt, JWTError
from app.config import settings
from datetime import datetime, timezone

from app.users.dao import UserDAO
from app.users.models import Users

from exceptions import (
        UserIsNotPresentException,
        TokenAbsentException,
        IncorrectTokenFormatException,
        TokenExpiredException,
        ThisUserHasNoRights
    )


def get_token(request: Request):
    token = request.cookies.get("todo_access_token")
    if not token:
        raise TokenAbsentException()
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise IncorrectTokenFormatException()

    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.now(timezone.utc).timestamp()):
        raise TokenExpiredException()

    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException()

    user = await UserDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException()

    return user


def get_admin_user(current_user: Users = Depends(get_current_user)):
    if current_user.role != 2:
        raise ThisUserHasNoRights()
    return current_user
