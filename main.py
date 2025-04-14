from fastapi import FastAPI
from  enum import Enum

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.post("/")
async def post():
    return {"message": "Hello from the Post Route"}

@app.put("/")
async def put():
    return {"message": "Hello from the Put Route"}

@app.get("/users")
async def list_users():
    return {"message": "List of users"}

@app.get("/user/me")
async def get_current_user():
    return {"user_id": "me"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "Message": "You are healthy!"}

    if food_name.value == 'fruits':
        return {"food_name": food_name, "Message": "You are still healthy but like sweet things!"}

    return {"food_name": food_name, "Message": "You are not healthy!"}

@app.get("/items")
async def list_items():
    return {"items": []}