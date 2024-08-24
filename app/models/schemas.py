from datetime import datetime
from typing import List, Union

from pydantic import BaseModel, field_validator


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

    @staticmethod
    def contains_digit(s):
        return any(char.isdigit() for char in s)


    @field_validator('First_name')
    def check_first_name(cls, v):

        if (cls.contains_digit(v)):
            raise ValueError('First_name не может содержать цифры')
        return v

    @field_validator('Last_name')
    def check_Last_name(cls, v):
        if cls.contains_digit(v):
            raise ValueError('Last_name не может содержать цифры')

        return v


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []