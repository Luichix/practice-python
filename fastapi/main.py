from enum import Enum
from typing import Annotated
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, date, timedelta
from uuid import UUID

# pip install python-multipart
# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import HTMLResponse

# import pydantic

# print("version", pydantic.__version__)

app = FastAPI()

fake_elements_db = [
    {"element_name": "Foo"},
    {"element_name": "Bar"},
    {"element_name": "Boo"},
]


class Image(BaseModel):
    url: HttpUrl
    name: str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "url": "https://avatars.githubusercontent.com/u/73667747?s=400&v=4",
                    "name": "Luichix",
                }
            ]
        }
    }


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None,
        title="The description of the item",
        max_length=300,
        examples=["A very nice item"],
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    is_offer: bool | None = None
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


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


@app.post("/offers/")
async def create_offer(offer: Offer) -> Offer:
    return offer


@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]) -> list[Image]:
    return images


@app.post("/index-weights")
async def create_index_weights(weights: dict[int, float]):
    return weights


@app.put("/process/{process_id}")
async def update_process(
    process_id: UUID,
    start_datetime: Annotated[datetime | None, Body()] = None,
    end_datetime: Annotated[datetime | None, Body()] = None,
    repeat_at: Annotated[date | None, Body()] = None,
    process_after: Annotated[timedelta | None, Body()] = None,
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": process_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


# @app.post("/files/")
# async def create_files(
#     files: Annotated[list[bytes], File(description="Multiple files as bytes")],
# ):
#     return {"file_sizes": [len(file) for file in files]}


# @app.post("/uploadfiles/")
# async def create_upload_files(
#     files: Annotated[
#         list[UploadFile], File(description="Multiple files as UploadFile")
#     ],
# ):
#     return {"filenames": [file.filename for file in files]}


# @app.get("/html-files")
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)
