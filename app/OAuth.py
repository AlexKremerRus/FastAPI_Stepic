from fastapi import FastAPI, Depends, Header, status, HTTPException, Response
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from models.schemas import Autorization
import for_jwt
import jwt
from typing import Annotated

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

@app.get("/protected")
async def protected_route(Authorization_1: Annotated[str | None, Header()]= None):
    # response = Response(headers={"Authorization":Authorization})
    # print(f"response: {response}")
    user = for_jwt.get_user_from_token(Authorization_1)

    print(f"Authorization: {Authorization_1}")
    print(f"user: {user}")

    if user:
        return {"message": "You have access to the protected resource!", "user_info": user}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
# test_agent_1: Annotated[str | None, Header()]= None