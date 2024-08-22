
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/index")
def hello():
    return FileResponse("index.html")