from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    username: str
    disable: Union[bool, None] = None


class UserInDB(User):
    password: str
