from fastapi import FastAPI,Depends,Body
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib import fastapi
# from starlette.middleware.sessions import SessionMiddleware
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from src.config.tortoise_conf import TORTOISE_ORM as db_config
from src.config import settings
from src.apps import routers
from fastapi.staticfiles import StaticFiles
from src.apps.edvora.endpoints import get_current_login
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import logging
from src.config.settings import STATIC_ROOT
from src.config.settings import sio, CHAT_MICROSERVICE_HOST
import json
from fastapi.responses import HTMLResponse

# fastapi.logging = logging.getLogger('uvicorn')
tags_metadata = [
    {
        "name": "broadcast",
        "description": "Operations with sockets. connect and send message message",
    },
    
]
app = FastAPI(
    title="Edvora",
    description="Edvora assignment",
    version="0.1.0",
    openapi_tags=tags_metadata,
)



app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")
app.mount("/public", StaticFiles(directory="public"), name="public")
app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=[
        "192.168.29.98", '192.168.29.12', '192.168.29.242', 'localhost', '127.0.0.1','*']
)

    

    # return "hello"

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("shutdown")
async def shutdown_db_client():
    destroy_clients()
    
@app.get("/connectBroadcast",tags=['broadcast'])
async def get_socket(session:str = Depends(get_current_login)):
    html = ""
    print(str(STATIC_ROOT)+"/index.html")
    with open(f"{STATIC_ROOT}/index.html", "r") as file:
        html = file.read()
    return HTMLResponse(html)

@app.post("/sendMessage",tags=['broadcast'])
async def send_broadcast_message(message:str=Body(...),session:str = Depends(get_current_login)):
    data = dict()
    data['username'] = session
    data['message'] = message
    json_object = json.dumps(data)
    await sio.emit('send_broadcast_message',json_object)
    return data  

 



@app.on_event("startup")
async def start_db():
    init_tortoise()
    await sio.connect(CHAT_MICROSERVICE_HOST)

    # await connect_chat_server()





db_config["generate_schemas"]=False
db_config["add_exception_handlers"]=True

# app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
app.include_router(routers.api_router, prefix=settings.API_V1_STR)


# register_tortoise(app, config=db_config)
def init_tortoise():
    register_tortoise(
        app,
        db_url=settings.DATABASE_URI,
        modules={"models": settings.APPS_MODELS},
        generate_schemas=False,
        add_exception_handlers=True,
    )
    print("tortoise connected successfully")
    


    
