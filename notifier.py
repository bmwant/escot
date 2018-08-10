import asyncio

import aiohttp

import config


ENDPOINT_TEMPLATE = 'https://api.telegram.org/bot{bot_api_key}/sendMessage'


async def send_message(message):
    url = ENDPOINT_TEMPLATE.format(bot_api_key=config.TELEGRAM_BOT_TOKEN)
    params = {
        'chat_id': '@escot',
        'text': message,
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            print(resp.status)


async def notify():
    from fetcher import get_current_price
    price = await get_current_price()
    message = 'Current bitcoin price is {}$'.format(price)
    await send_message(message)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(notify())
