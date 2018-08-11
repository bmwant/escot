import os
import base64
import asyncio

import jinja2
import aiohttp_session
import aiohttp_jinja2
from aiohttp import web
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography import fernet

import config
from app import views
from app.fetcher import get_current_price
from app.notifier import send_message
from app.utils import logger


async def fetch_price():
    while True:
        logger.debug('Checking current price...')
        price = await get_current_price()
        message = 'Current  bitcoin price is {}$'.format(price)
        if config.NOTIFICATIONS_ENABLED:
            logger.debug('Sending message to a channel...')
            await send_message(message)
        await asyncio.sleep(config.POLL_PERIOD)


async def start_polling_price(app):
    app.loop.create_task(fetch_price())


def setup_routes(app):
    app.router.add_get('/', views.index)


def setup_static_routes(app):
    app.router.add_static(
        '/static/',
        path=os.path.join(config.PROJECT_ROOT, 'static'),
        name='static',
    )
    app.router.add_static(
        '/node_modules/',
        path=os.path.join(config.PROJECT_ROOT, 'node_modules'),
        name='node_modules',
    )


def configure_app():
    app = web.Application()
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    aiohttp_session.setup(app, EncryptedCookieStorage(secret_key))
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(config.TEMPLATES_DIR),
    )
    setup_routes(app)
    setup_static_routes(app)
    app.on_startup.append(start_polling_price)
    return app
