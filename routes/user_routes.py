from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from functions.jwt_functions import create_token, get_user_current
from functions.auth_functions import authentication_user
from fastapi import APIRouter, Depends
from datetime import timedelta
from db.fake_db import db


user = APIRouter()

oauth2 = OAuth2PasswordBearer("/token")


@user.get("/")
def home():
    return "hello world."


@user.get("/users/me")
def users(token: str = Depends(oauth2)):
    user = get_user_current(token)
    return user


@user.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authentication_user(form_data.username, form_data.password, db)
    access_token_expires = timedelta(minutes=30)
    access_token_jwt = create_token({"sub": user.username}, access_token_expires)
    return {
        "access_token": access_token_jwt,
        "token_type": "bearer"
    }
