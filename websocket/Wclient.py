import asyncio
import websockets

async def run_client():
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        print(" Connect Server ได้")
        while True:
            msg = input("นายอยากคุยอะไร")
            if msg  == "exit":
                break
            await websocket.send(msg)
            print(f" Send: {msg}")

            response = await websocket.recv()
            print(f" ตอบกลับมาว่า: {response}")

if __name__ == "__main__":
    asyncio.run(run_client())