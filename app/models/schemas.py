from datetime import datetime
from typing import List, Union

from pydantic import BaseModel, field_validator
import re

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

class Person(BaseModel):
    username: str
    enail: str | None = None
    age: int | None = None
    is_subscribed : bool = False

    @staticmethod
    def is_valid_email(email: str) -> bool:
    # Регулярное выражение для проверки email-адреса
        email_regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
        return re.match(email_regex, email) is not None


    # @field_validator('username')
    # def check_username(cls, v):
    #     if v.isalnum():
    #         raise ValueError('username не может содержать цифры')
    #     return v

    @field_validator('age')
    def check_age(cls, v):
        if v < 0:
            raise ValueError('age не может быть отрицательным')
        elif v>100:
            raise ValueError('age не может быть больше 100')
        return v

    @field_validator('enail')
    def check_enail(cls, v):
        if not cls.is_valid_email(v):
            raise ValueError('email не соответствует требованиям')
        return v


class SampleProduct(BaseModel):
    product_id: int
    name: str
    category: str
    price: float

class Autorization(BaseModel):
    login: str
    password: str

