from datetime import datetime
from typing import List, Union

from pydantic import BaseModel,field_validator



# создаём модель данных, которая обычно расположена в файле models.py
class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []

    @field_validator('id')
    def check_age(cls, v):
        if v < 0:
            raise ValueError('Нельзя присваивать полю id отрицательное значение')
        return v

    @field_validator('name')
    def check_name(cls, v):
        if any(char.isdigit() for char in v):
            raise ValueError('Name не может содержать цифры')
