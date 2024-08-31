from fastapi import FastAPI, Depends, status, HTTPException

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models.schemas import Autorization
from models.sample import USER_DATA

app = FastAPI()
security = HTTPBasic()

def get_user_from_db(username: str):
    for user in USER_DATA:
        if user.login == username:
            return user
    return None

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user_from_db(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials", headers={"WWW-Authenticate": "Basic"})
    return user

@app.get("/protected_resource/")
def get_protected_resource(user: Autorization = Depends(authenticate_user)):
    return {"message": "You have access to the protected resource!", "user_info": user}
