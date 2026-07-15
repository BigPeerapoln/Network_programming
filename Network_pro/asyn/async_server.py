import asyncio
from aiohttp import web
import socketio
from json import dumps

# สร้าง Async Socket.IO Server
sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)

@sio.event
async def join_chat(sid, message):
    # ป้องกัน KeyError ด้วยการใช้ .get() เผื่อค่าส่งมาไม่ครบ
    name = message.get('name', sid)
    room = message.get('room', 'default_room')
    print(f"{name} joined to {room}")
    sio.enter_room(sid, room)

@sio.event
async def exit_chat(sid, message):
    room = message.get('room', 'default_room')
    sio.leave_room(sid, room)

@sio.event
async def send_chat_room(sid, message):
    # แก้ไขจุดพิม์ผิด: เปลี่ยนจาก message[' room' ] (มีเว้นวรรค) เป็น message.get('room')
    room = message.get('room')
    msg_content = message.get('message', '')
    sender_name = message.get('name', sid)
    
    # ส่งข้อความไปยังห้องที่กำหนด
    await sio.emit('get_message', {
        'message': msg_content, 
        'from': sender_name
    }, room=room)

@sio.event
async def connect(sid, environ):
    print(f"Client connected: {sid}")
    await sio.emit('my_response', {'data': 'Connected', 'count': 0}, room=sid)

@sio.event
def disconnect(sid):
    print(f'Client disconnected: {sid}')

if __name__ == '__main__':
    # กำหนด host และ port ให้ชัดเจนเป็น 127.0.0.1 และพอร์ต 8080 ตรงกับฝั่ง Client
    web.run_app(app, host='127.0.0.1', port=8080)