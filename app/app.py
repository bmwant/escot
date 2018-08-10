import asyncio
import base64

import aiohttp
import aiohttp_session
from aiohttp import web
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography import fernet

import config
from app.fetcher import get_current_price
from app.notifier import send_message
from app.utils import logger


async def index(request):
    return web.Response(text='List of transactions')


async def fetch_price():
    while True:
        logger.debug('Sending healthcheck...')
        price = await get_current_price()
        message = 'Currentl  bitcoin price is {}$'.format(price)
        await send_message(message)
        await asyncio.sleep(config.POLL_PERIOD)


async def start_polling_price(app):
    app.loop.create_task(fetch_price())


def setup_routes(app):
    app.router.add_get('/', index)


def configure_app():
    app = web.Application()
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    aiohttp_session.setup(app, EncryptedCookieStorage(secret_key))
    setup_routes(app)
    app.on_startup.append(start_polling_price)
    return app
