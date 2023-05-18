from fastapi.exceptions import HTTPException


def http_exception():
    return HTTPException(
        status_code=401,
        detail="User not found.",
        headers={"WWW-Authenticate": "Bearer"},
    )

def http_exception2():
    return HTTPException(
        status_code=400,
        detail="Not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

