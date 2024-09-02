from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from models.schemas import Autorization
import for_jwt
import jwt


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



# роут для аутентификации; так делать не нужно, это для примера - более корректный пример в следующем уроке
@app.post("/login_OAuth2")
async def login(user_in: Autorization):
    for user in for_jwt.USERS_DATA:
        if user.get("username") == user_in.login and user.get("password") == user_in.password:
            return {"access_token": for_jwt.create_jwt_token({"sub": user_in.login}), "token_type": "bearer"}
    return {"error": "Invalid credentials"}


# защищенный роут для получения информации о пользователе
@app.get("/about_me")
async def about_me(current_user: str = Depends(for_jwt.get_user_from_token)):
    user = for_jwt.get_user(current_user)
    if user:
        return user
    return {"error": "User not found"}
