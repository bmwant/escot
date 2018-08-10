import asyncio
from http import HTTPStatus

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
