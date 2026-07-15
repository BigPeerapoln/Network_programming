import asyncio

async def hanlek(a,b):
    print('%s/%s'%(a,b))
    return a/b

# loop = asyncio.get_event_loop()
# phophan = loop.run_until_complete(hanlek(7,6))
phonhan = asyncio.run(hanlek(7,6))
print("ผลลัพธ์: %.3f" %phonhan)
