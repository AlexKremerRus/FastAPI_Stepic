
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/index")
def hello():
    return FileResponse("index.html")

@app.post("/calculation_v1")
def calculation_v1(num_1, num_2):
    return {"result": int(num_1) + int(num_2)}


