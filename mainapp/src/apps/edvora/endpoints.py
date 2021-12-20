from .auth import verify_password, get_password_hash
import uuid
from starlette.responses import JSONResponse
# from starlette.requests import Request
from starlette import status
from .models import *
from src.config.settings import BASE_DIR, STATIC_ROOT,SECRET_KEY
from fastapi import APIRouter, Depends, BackgroundTasks, Response, status, Request, File, UploadFile, Body, HTTPException
from tortoise.query_utils import Q
import pathlib
from typing import List, Optional
import os
import shutil
from .service import *
from .schema import *
from jose import jwt
import requests
from starlette.responses import RedirectResponse
from .pydanticmodels import *
from fastapi_pagination import LimitOffsetPage, Page, add_pagination
from fastapi_pagination.ext.tortoise import paginate
from fastapi.security import APIKeyCookie
from fastapi.responses import HTMLResponse

from datetime import datetime,date,timedelta
import os
import aiohttp
from .pydanticmodels import CREATE_USER

edvora_assignment = APIRouter()
cookie_sec = APIKeyCookie(name="session")

def get_current_login(session:str = Depends(cookie_sec)):
    try:
        data = jwt.decode(session, SECRET_KEY)
        data = jwt.decode(session, SECRET_KEY)
        date = data['expires'].split("-")
        expiry_date = datetime(int(date[0]),int(date[1]),int(date[2]))
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication"
        )
    if expiry_date < datetime.now():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Token Expires Login Again"
        )
    return data['username']

@edvora_assignment.post('/registerUser')
async def register_user(user: CREATE_USER):
    user = await broadcast_user.user_create(user)
    return {"success":"user created successfully","user":user}

   


@edvora_assignment.post('/login')
async def save_cookie_user(response: Response, request: Request, username: str = Body(...), password: str = Body(...)):
    if await broadcast_user.authenticate(username,password):
        expire = date.today() + timedelta(days=15)
        token = jwt.encode({"username": username, "expires": str(expire)}, SECRET_KEY)
        response.set_cookie("session", token)
        return {"success":f"{username} you can now connect to the broadcast now you can send and receive messages"}
    else:
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Invalid user or password or register first and try out"
            )
@edvora_assignment.post('/sendMessage')
async def send_message(message:str,username:str = Depends(get_current_login)):
    html = ""
    with open(f"{STATIC_ROOT}/index.html", "r") as file:
        html = file.read()
    return HTMLResponse(html)


@edvora_assignment.get('/logout')
async def logout(response: Response, request: Request, session: str = Depends(get_current_login)):
    user = await BroadCastUser.get(username=session)
    user.active = False
    await user.save()
    response.delete_cookie("session")
    return {"success":"user logout successfully"}





