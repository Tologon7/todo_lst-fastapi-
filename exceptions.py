from fastapi import HTTPException, status


class MainException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(
            status_code=self.status_code,
            detail=self.detail
        )


class TaskIsNotPresentException(MainException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Задача не найдена"


class UserIsNotPresentException(MainException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Пользователь не найден"


class UserAlreadyExistsException(MainException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Такой пользователь существует"


class TokenAbsentException(MainException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Остутствует токен"


class IncorrectTokenFormatException(MainException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Неправильный формат токена"


class TokenExpiredException(MainException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Истек время жизни токена"


class ThisUserHasNoRights(MainException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "У этого пользователя нету прав на данное действие"


class RoleAlreadyExistsException(MainException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Такая роль существует"
