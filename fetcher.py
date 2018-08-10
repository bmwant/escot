import asyncio

import aiohttp


REMOTE_URL = 'https://blockchain.info/ticker'
CURRENCY = 'USD'


async def get_current_price():
    async with aiohttp.ClientSession() as session:
        async with session.get(REMOTE_URL) as resp:
            data = await resp.json()
            return data[CURRENCY]['last']


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(get_current_price()))
