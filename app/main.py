
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from models.schemas import User, Item, Person
from typing import Annotated
from models.sample import sample_products

app = FastAPI()

@app.get("/index")
async def hello():
    return FileResponse("index.html")

@app.get('/user_id/{user_id_v1}') # тут объявили параметр пути
async def search_user_by_id(user_id_v1: int, is_admin: bool = False): # тут указали его тип данных
    # какая-то логика работы поиска
    return {"вы просили найти юзера с id": user_id_v1, "является ли он админом": is_admin}

@app.post("/calculation_v1")
async def calculation_v1(num_1, num_2):
    return {"result": int(num_1) + int(num_2)}

@app.post("/create_user_v1")
async def create_user_v1(user: User):
    return {"name": user.First_name + " " + user.Last_name}

@app.post("/items_v1")
async def create_item(item: Item) -> Item:
    return item

@app.get("/items_v1")
async def read_items() -> list[Item]:
    return [
        Item(name="Foo", price=42.0),
        Item(name="Bar", price=43.0)
            ]

@app.post("/file_v1/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/file_v2/")
async def create_file_2(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/uploadfile_v1/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@app.get("/test/query")
async def test_query(query_param: str):
    return {"message": f"Hello World {query_param}"}


@app.post("/create_person_v1")
async def create_person(person: Person):
    return f"{person.username} - подписан? - {person.is_subscribed}"

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    for product in sample_products:
        if product["product_id"] == product_id:
            return product
    else:
        return {"message": "Такого продукта нет"}

@app.get("/get_products_search")
async def search_product(keyword: str, category: str | None = None, limit: int | None = None):
    search_answer = []
    for product in sample_products:
        if keyword.lower() in product["name"].lower():
            if category is None or product["category"] == category:
                search_answer.append(product)
    if limit is not None:
        search_answer = search_answer[:limit]
    return search_answer
