
from fastapi import FastAPI
from fastapi.responses import FileResponse
from models.schemas import User

app = FastAPI()

@app.get("/index")
def hello():
    return FileResponse("index.html")

@app.post("/calculation_v1")
def calculation_v1(num_1, num_2):
    return {"result": int(num_1) + int(num_2)}

@app.post("/create_user_v1")
def create_user_v1(user: User):
    return {"name": user.name}