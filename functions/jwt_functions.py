from functions.exceptions import http_exception, http_exception2
from functions.auth_functions import get_user
from datetime import datetime, timedelta
from dotenv import load_dotenv
from jose import jwt, JWTError
from schemas.user import User
from fastapi import Depends
from db.fake_db import db
from typing import Union
import os

load_dotenv()


def create_token(data: dict, time_expire: Union[datetime, None] = None):
    data_copy = data.copy()
    if time_expire == None:
        expire = datetime.utcnow() + timedelta(minutes=15)
    else:
        expire = datetime.utcnow() + time_expire
    data_copy.update({"exp": expire})
    return jwt.encode(
        data_copy, key=os.environ["SECRET_KEY"], algorithm=os.environ["ALGORITHM"]
    )


def get_user_current(token):
    try:
        token_decode = jwt.decode(
            token, key=os.environ["SECRET_KEY"], algorithms=[os.environ["ALGORITHM"]]
        )
        username = token_decode.get("sub")
        if username == None:
            raise http_exception()
    except JWTError:
            raise http_exception()
    user = get_user(username, db)
    if not user:
        raise http_exception()
    else:
        if user.disable:
            raise http_exception2()
        else:
            return user
     