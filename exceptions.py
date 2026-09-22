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
