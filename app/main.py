from fastapi import FastAPI
from app.controller import user_controller as user_router

app = FastAPI()

@app.get("/")
def index():
    return "Ola mundo"

app.include_router(user_router)
