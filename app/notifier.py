from http import HTTPStatus

import aiohttp

import config
from app.utils import logger


ENDPOINT_TEMPLATE = 'https://api.telegram.org/bot{bot_api_key}/sendMessage'


async def send_message(message):
    url = ENDPOINT_TEMPLATE.format(bot_api_key=config.TELEGRAM_BOT_TOKEN)
    params = {
        'chat_id': config.CHAT_ID,
        'text': message,
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            if resp.status != HTTPStatus.OK:
                text = await resp.text()
                logger.error(f'Error {resp.status}: {text}')
