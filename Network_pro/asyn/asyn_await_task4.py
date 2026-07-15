import asyncio

async def buaklek(a,b):
   c = a + b
   print("==ฟังชันก์เริ่มทำงาน==")
   return c
async def main():
   coru = buaklek(13,10)
   task = asyncio.create_task(coru)
   phonbuak = await task
   print("ได้ผลบวก %s" %phonbuak)

maincore = main()
asyncio.run(maincore)