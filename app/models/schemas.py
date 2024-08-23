from datetime import datetime
from typing import List, Union

from pydantic import BaseModel,field_validator


class User(BaseModel):
    id: int
    First_name: str = "John"
    Last_name: str = "Doe"
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []

    @field_validator('id')
    def check_id(cls, v):
        if v < 0:
            raise ValueError('Нельзя присваивать полю id отрицательное значение')
        return v

# TODO: доделать валидацию
    # @field_validator('First_name')
    # def check_first_name(cls, v):

    #     if (any(char.isdigit() for char in v)):
    #         raise ValueError('First_name не может содержать цифры')

    # @field_validator('First_name')
    # def check_Last_name(cls, v):
    #     if any(char.isdigit() for char in v):
    #         raise ValueError('Last_name не может содержать цифры')
