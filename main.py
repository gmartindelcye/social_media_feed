from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, List
from db import users
from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(plain_password: str) -> str:
    return pwd_ctx.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_ctx.verify(plain_password, hashed_password)


class Notification(BaseModel):
    author: str
    description: str


class User(BaseModel):
    name: str
    username: str
    email: str
    birthday: str
    friends: List[str]
    notifications: List[Notification]


class UserDB(User):
    hashed_password: str


app = FastAPI()
templates = Jinja2Templates('templates')
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/', response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse('index.html', {"request": request, "title": "FriendConnect - Home"})


@app.get('/login', response_class=HTMLResponse)
def get_login(request: Request):
    return templates.TemplateResponse('login.html', {"request": request, "title": "FriendConnect - Login"})