import asyncio

writers = []

# ปรับให้ฟังก์ชัน forward เป็น async เพื่อสั่ง drain (เคลียร์ท่อข้อมูล) ให้คนอื่นได้ด้วย
async def forward(sender_writer, addr, message):
    for w in writers:
        # ส่งให้ทุกคนยกเว้นตัวเอง
        if w != sender_writer:
            try:
                w.write(f"{addr!r} : {message}\n".encode())
                await w.drain() # รอให้ข้อมูลส่งถึงคนอื่นอย่างปลอดภัย
            except ConnectionError:
                # ถ้าคนอื่นหลุดไปแล้วแต่ยังไม่ได้ลบชื่อออก ให้ข้ามไปก่อน
                pass

async def handle(reader, writer):
    writers.append(writer)
    addr = writer.get_extra_info('peername')
    
    connect_msg = f"{addr!r} joined the chat!"
    print(connect_msg)
    await forward(writer, "System", connect_msg)
    
    try:
        while True:
            data = await reader.read(100)
            
            # ดักจับ: ถ้า Client ปิดหน้าต่างหนี (data ว่าง) ให้หลุดลูป
            if not data:
                break
                
            message = data.decode().strip()
            
            if message == "exit":
                break
                
            # ส่งข้อความที่พิมพ์ ไปหาผู้เล่นคนอื่นทุกคน
            await forward(writer, addr, message)
            
    finally:
        # ย้ายขั้นตอนการถอดถอนและปิดการเชื่อมต่อมาไว้ที่นี่ (นอกลูป while)
        # เพื่อให้ทำงานชัวร์ๆ ไม่ว่าเขาจะพิมพ์ exit หรือปิดโปรแกรมหนี
        if writer in writers:
            writers.remove(writer)
            
        exit_msg = f"{addr!r} left the chat."
        print(exit_msg)
        
        # แจ้งบอกคนในห้องแช็ตที่เหลือว่าคนนี้ออกไปแล้ว
        await forward(None, "System", exit_msg)
        
        writer.close()
        try:
            await writer.wait_closed()
        except ConnectionError:
            pass

async def main():
    server = await asyncio.start_server(
        handle, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever()

asyncio.run(main())