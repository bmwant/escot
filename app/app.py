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
from app import views, filters
from app.fetcher import get_current_price
from app.notifier import send_message
from app.engine import check_transactions
from app.utils import logger





async def start_polling_price(app):
    task = app.loop.create_task(fetch_price())
    app['tasks'].append(task)


async def start_checkin_transactions(app):
    task = app.loop.create_task(check_transactions())
    app['tasks'].append(task)


async def close_tasks(app):
    for task in app.get('tasks', []):
        logger.debug('Cancelling task %s...', task._coro.__name__)
        task.cancel()


def setup_routes(app):
    app.router.add_get('/', views.index)
    app.router.add_post('/transaction/add', views.transaction_add)
    app.router.add_get('/transaction/close', views.transaction_close)


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
    app['tasks'] = []
    app['logger'] = logger
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    aiohttp_session.setup(app, EncryptedCookieStorage(secret_key))
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(config.TEMPLATES_DIR),
        filters={
            'checkbox': filters.checkbox,
            'format_time': filters.format_time,
            'format_datetime': filters.format_datetime,
        },
    )
    setup_routes(app)
    setup_static_routes(app)
    app.on_startup.append(start_polling_price)
    app.on_shutdown.append(close_tasks)
    return app
