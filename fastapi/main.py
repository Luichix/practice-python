from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None 


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    letnet = "letnet"

@app.get("/") 
async def read_root():
    return { "Hello" : "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str |None = None):
    return {"item_id": item_id, "q": q }

@app.put("/items/{items_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/users")
async def read_users():
    return ["Luichix", "Manu"]

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "The current user"}

@app.get("/users/{user_id}")
async def read_user(user_id:str):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FWT!" }
    
    if model_name is ModelName.letnet:
        return {"model_name": model_name, "message": "LeCNN all the images" }
    
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}