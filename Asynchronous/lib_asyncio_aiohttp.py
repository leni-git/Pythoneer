import aiohttp
import asyncio

async def fetch(index, session, url):
    print('{} Start_fetch >> {}'.format(index, url))
    async with session.get(url) as response:
        return await response.text()

async def main(index, url):
    print('{} Start_main >> {}'.format(index, url))
    async with aiohttp.ClientSession() as session:
        html = await fetch(index, session, url)
        print(html)

if __name__ == '__main__':
    ulrs = ['http://naver.com', 'http://python.org', 'http://google.com']
    futures = [main(index, url) for index, url in enumerate(ulrs)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
