import asyncio,aiohttp

async def aioioio():
    async with aiohttp.ClientSession() as ses:
        url = "https://www.youtube.com/"
        async with ses.get(url) as r :
            print('url: ' , r.url)
            print("status: ", r.status)
            print("charset: ", r.charset)
asyncio.run(aioioio())
