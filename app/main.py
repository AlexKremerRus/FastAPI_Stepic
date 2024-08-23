
from fastapi import FastAPI
from fastapi.responses import FileResponse
from models.schemas import User

app = FastAPI()

@app.get("/index")
async def hello():
    return FileResponse("index.html")

@app.get('/{user_id_v1}') # тут объявили параметр пути
async def search_user_by_id(user_id: int): # тут указали его тип данных
    # какая-то логика работы поиска
    return {"вы просили найти юзера с id": user_id}

@app.post("/calculation_v1")
async def calculation_v1(num_1, num_2):
    return {"result": int(num_1) + int(num_2)}

@app.post("/create_user_v1")
async def create_user_v1(user: User):
    return {"name": user.First_name + " " + user.Last_name}