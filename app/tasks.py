import asyncio

import config
from app.utils import logger
from app.fetcher import get_current_price
from app.engine import check_transactions
from app.notifier import send_message


async def fetch_price_task():
    while True:
        logger.debug('Checking current price...')
        price = await get_current_price()
        message = 'Current  bitcoin price is {:.2f}$'.format(price)
        if config.NOTIFICATIONS_ENABLED:
            logger.debug('Sending message to a channel...')
            await send_message(message)
        await asyncio.sleep(config.POLL_PRICE_PERIOD)


async def check_transactions_task():
    while True:
        logger.debug('Checking transactions to close...')
        await check_transactions()

        await asyncio.sleep(config.CHECK_TRANSACTIONS_PERIOD)
