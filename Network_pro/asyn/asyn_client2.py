import asyncio
from socketio import AsyncClient
from aioconsole import ainput

# === ⚙️ ตั้งค่าข้อมูลการเชื่อมต่อ ===
IpAddress = '10.4.15.33'  
PORT = '8080'            
clientName = 'Deadpool2'  
roomName = 'Marvel'      

sio = AsyncClient()
FullIp = f"http://{IpAddress}:{PORT}"

@sio.event
async def connect():
    print('Connected to server!')
    # ส่งคำขอเข้าร่วมห้องแช็ตทันที
    await sio.emit('join_chat', {'room': roomName, 'name': clientName})

@sio.event
async def get_message(message):
    sender = message.get('from', 'Unknown')
    msg_text = message.get('message', '')
    
    # แสดงผลข้อความบนหน้าจอ Client
    if clientName == sender:
        print(f"You : {msg_text}")
    else:
        print(f"{sender} : {msg_text}")

# --- จุดแก้ไขที่ 1: ปรับเอา sleep ออก เพื่อให้กวาดรับคีย์บอร์ดได้ทันทีไม่ขัด Event Loop ---
async def send_message():
    while True:
        # ainput จะหยุดรอรับคีย์บอร์ดแบบ Async อยู่แล้ว ไม่ต้องใช้ sleep คั่น
        messageToSend = await ainput() 
        
        # ส่งข้อความไปยังเซิร์ฟเวอร์
        if messageToSend.strip():  # ไม่ส่งข้อความว่าง
            await sio.emit('send_chat_room', {
                'message': messageToSend, 
                'name': clientName, 
                'room': roomName
            })

async def connectToServer():
    try:
        await sio.connect(FullIp)
        await sio.wait()
    except Exception as e:
        print(f"Connection failed: {e}")

async def main():
    # ใช้ asyncio.gather รันสองอย่างควบคู่กันอย่างสมดุล
    await asyncio.gather(
        connectToServer(),
        send_message()
    )

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nDisconnected.")