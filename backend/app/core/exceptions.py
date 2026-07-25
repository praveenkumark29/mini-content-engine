from fastapi import HTTPException, status


class JobNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found",
        )


class InvalidImageException(HTTPException):
    def __init__(self, detail: str = "Invalid image file"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
        )