import asyncio

async def handle(reader, writer):
    addr = writer.get_extra_info("peername")
    message = f"{addr!r} is connected !!!!!"
    print(message)
    
    try:
        while True:
            data = await reader.read(100)
            
            # แก้ไขบั๊กที่ 2: ถ้าไม่มีข้อมูลส่งมา (Client ปิดการเชื่อมต่อหนี) ให้หลุดลูปทันที
            if not data:
                print(f"{addr!r} disconnected abruptly.")
                break
                
            message = data.decode().strip()
            
            # ส่งข้อมูลสะท้อนกลับไปหา Client
            writer.write(data)
            await writer.drain()
            
            if message == "exit":
                message = f"{addr!r} wants to close the connection."
                print(message)
                break
            print(message)
    finally:
        # ย้าย writer.close() มาไว้ที่นี่ เพื่อให้มั่นใจว่าจะปิดการเชื่อมต่อแน่นอนแม้เกิดข้อผิดพลาด
        print(f"Closing connection for {addr!r}")
        writer.close()
        await writer.wait_closed() # แนะนำให้เพิ่ม บรรทัดนี้ใน Python 3 เพื่อความสะอาดในการเคลียร์ Memory

async def main():
    server = await asyncio.start_server(
        handle, "127.0.0.1", 8888)
    
    # แก้ไขบั๊กที่ 1: เปลี่ยนจาก .socket[0] เป็น .sockets[0] เพื่อรองรับ Python 3.14
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")
    
    async with server:
        await server.serve_forever()

asyncio.run(main())