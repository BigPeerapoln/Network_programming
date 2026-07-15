import asyncio
import time

async def ioioio(wela, chue_ngan):
    print("เริ่ม %s เวลาผ่านไปแล้ว %.5f วินาที" % (chue_ngan, time.time() - t0))
    await asyncio.sleep(wela)
    print("เสร็จแล้ว %s เวลาผ่านไปแล้ว %.5f วินาที" % (chue_ngan, time.time() - t0))
    return

async def main():
    # ใช้ asyncio.gather รันทุก coroutines ไปพร้อมกันได้ทันที
    await asyncio.gather(
        ioioio(1.5, "โหลดเพลง"),
        ioioio(2.5, "โหลดอนิเมะ"),
        ioioio(0.5, "โหลดหนัง"),
        ioioio(2, "โหลดเกม")
    )

t0 = time.time()
asyncio.run(main())