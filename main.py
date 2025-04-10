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


cla

