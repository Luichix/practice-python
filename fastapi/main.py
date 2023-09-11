from enum import Enum
from typing import Annotated
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel

app = FastAPI()

fake_elements_db = [
    {"element_name": "Foo"},
    {"element_name": "Bar"},
    {"element_name": "Boo"},
]


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    is_offer: bool | None = None
    tax: float | None = None


class User(BaseModel):
    fullname: str
    username: str


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    letnet = "letnet"


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


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
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FWT!"}

    if model_name is ModelName.letnet:
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/elements/")
async def read_element(skip: int = 0, limit: int = 10):
    return fake_elements_db[skip : skip + limit]


@app.get("/items/query/{item_id}")
async def read_itemquery(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/users/{user_id}/items/{items_id}")
async def read_user_items(
    user_id: str, item_id: str, needy: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "user_id": user_id, "needy": needy}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is a long description for this item"})
    return item


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax: item.tax + item.price
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/body/{item_id}")
async def update_item_body(item_id: str, item: Item):
    return {"item_id": item_id, **item.model_dump()}


@app.put("/items/body_query/{item_id}")
async def update_item_body_query(item_id: str, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result


@app.get("/fruit/")
async def read_fruit(
    q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="\S")] = None
):
    # For Required params use: "Required" or Elipsis "..."
    # Also you can remove Nove or Query(default=None)
    # Can you use both: Declare type None and set Requerid Param
    result = {"fruits": [{"fruit_name": "apple"}, {"fruit_name": "banana"}]}
    if q:
        result.update({"q": q})
    return result


@app.get("/fruits/list/")
async def read_fruits_list(
    q: Annotated[
        list[str],
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            alias="item-query",
            deprecated=True,
            include_in_schema=True,
        ),
    ] = ["apple", "banana"]
):
    query_items = {"q": q}
    return query_items


@app.get("/fruits/{fruit_mount}")
async def read_fruits_list(
    fruit_id: Annotated[
        int, Path(title="This title is for path parameter", ge=1, le=10)
    ],
    q: Annotated[
        list[str],
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            alias="item-query",
            deprecated=True,
            include_in_schema=True,
        ),
    ] = ["apple", "banana"],
):
    query_items = {"q": q}
    return query_items


@app.put("/fruits_update/{fruit_id}")
async def update_fruit(
    item: Item,
    fruit_id: Annotated[int | None, Path(title="Path param")],
    user: User | None = None,
    q: Annotated[str | None, Query(title="query param")] = None,
    importance: Annotated[bool | None, Body()] = None,
):
    return {"fruit_id": fruit_id}
