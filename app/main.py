from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from model import UserRegistration
from db import DB
from typing import ClassVar


load_dotenv()

class Settings(BaseSettings):
    db: ClassVar = DB()

settings = Settings()
app = FastAPI()

@app.get("/reset_table")
async def reset_table():
    settings.db.create_table()

@app.get("/users")
async def intro():
    return settings.db.get_users()

@app.post("/reg")
async def registration(User: UserRegistration):
    
    settings.db.reg_user(User)
    return {"res": True}

if __name__ == '__main__':
    uvicorn.run("main:app", port=8081, log_level='info')
