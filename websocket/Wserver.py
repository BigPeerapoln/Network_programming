import asyncio
import websockets

async def handle_client(websocket):
    print(" Client connected!")
    try:
        async for message in websocket:
            print(f" ได้รับข้อความจาก Client: {message}")

            reply = f"Server ได้รับข้อความ '{message}' เรียบร้อยแล้ว!"
            await websocket.send(reply)
            print("ส่งตอบกลับเรียบร้อย")

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected!")

async def main():

    async with websockets.serve(handle_client,"localhost",8765):
        print("Websocket Server กำลังทำงานที่ ws://localhost:8765")
        await asyncio.Future()
if __name__ == "__main__":
    asyncio.run(main())

