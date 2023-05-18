from functions.exceptions import http_exception
from passlib.context import CryptContext
from schemas.user import UserInDB
from db.fake_db import db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def authentication_user(username, password, db=db):
    user = get_user(username, db)
    if not user:
        raise http_exception()
    if not verify_pass(password, user.password):
        raise http_exception()
    return user


def get_user(username, db=db):
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)
    return []


def verify_pass(plane_pass, hashed_pass):
    return pwd_context.verify(plane_pass, hashed_pass)
