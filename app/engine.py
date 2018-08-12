from app.database import Transaction
from app.fetcher import get_current_price
from app.notifier import send_message
from app.utils import logger


async def check_transactions():
    current_price = await get_current_price()
    trans = Transaction.select().where(
        Transaction.date_closed.is_null(False) &
        (Transaction.rate_opened < current_price)
    )

    for t in trans:
        if current_price > t.rate_opened + t.diff:
            profit = t.calculate_profit(current_price)
            message = f'User {t.user.name} need to close his transaction ' \
                      f'#{t.id} to gain {profit}$'
            logger.info('Transaction #%s should be closed', t.id)
            send_message(message)
