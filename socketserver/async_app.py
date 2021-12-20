import socketio
sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins='*')
app = socketio.ASGIApp(sio,static_files={
    '/':'./public/'
})
GROUP_NAME = "PRIVATEBROADCAST"
@sio.event
async def connect(sid,environ):
    print(sid,"connected")
    sio.enter_room(sid,GROUP_NAME)
    success = {
        "success":"successfully connected to this group"
    }
    await sio.emit('broadcast_connect_success', success, to=sid)

@sio.event
async def disconnect(sid):
    print(sid,"disconnected")
    
@sio.event
async def broadcast_connect(sid):
    print("imheree")
    sio.enter_room(sid,GROUP_NAME)
    success = {
        "success":"successfully connected to this group"
    }
    await sio.emit('broadcast_connect_success', success, to=sid)
    

import json

@sio.event
async def send_broadcast_message(sid,data):
    print("imhereee")
    print(type(data))
    data = json.loads(data)
    print(type(data))
    print(data)
    await sio.emit('receive_broadcast_message',data,to=GROUP_NAME)

    

