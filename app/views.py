from datetime import datetime

import aiohttp_jinja2
from aiohttp import web
from app.database import Transaction, User


@aiohttp_jinja2.template('index.html')
async def index(request):
    records = Transaction.select()
    users = User.select()
    return {
        'users': users,
        'records': records,
    }



async def transaction_add(request):
    form = await request.post()
    user_id = form['user_id']
    amount = form['amount']
    diff = form['diff']
    rate_opened = form['rate_opened']

    t = Transaction.create(
        user=user_id,
        amount=amount,
        diff=diff,
        rate_opened=rate_opened,
    )
    print(t.user)
    return web.HTTPFound('/')


async def transaction_close(request):
    # tid = request.match_info.get('tid')
    tid = request.query.get('tid')
    rate_closed = request.query.get('rate_closed')
    transaction = Transaction.get(Transaction.id == tid)
    transaction.date_closed = datetime.now()
    transaction.rate_closed = rate_closed
    transaction.save()
    return web.HTTPFound('/')


async def transaction_delete(request):
    tid = request.match_info.get('tid')
    transaction = Transaction.get(Transaction.id == tid)
    transaction.delete_instance()
    return web.HTTPFound('/')
