from fastapi import HTTPException, status

UserNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="User not found"
)

UserNotExist = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Cannot delete an account that does not exist"
)
