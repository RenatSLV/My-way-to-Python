import aiohttp
import asyncio
import time

async def create_url_async(session, url):
    async with session.get(url) as response:
        return await response.text()
    
async def create_urls_async(urls):
    start = time.time()
    async with aiohttp.ClientSession() as session:
        task = [create_url_async(session, url) for url in urls]
        result = await asyncio.gather(*task)
        end = time.time()
        print(f"Асинхронное выполнение заняло {end - start} секунд")
        return result
    
urls = ["https://example.q-parser.ru/" for _ in range(100)]
asyncio.run(create_urls_async(urls))