import aiohttp
import asyncio

TARGET_URL = "https://ere-dv2x.onrender.com/recent-pets"
CONCURRENCY = 30
TIMEOUT = 10

async def ping(session, i):
    while True:
        try:
            async with session.get(TARGET_URL, timeout=TIMEOUT) as resp:
                print(f"[{i}] Status: {resp.status}")
        except Exception as e:
            print(f"[{i}] Error: {e}")
        await asyncio.sleep(0)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [ping(session, i) for i in range(CONCURRENCY)]
        await asyncio.gather(*tasks)

asyncio.run(main())
