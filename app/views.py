import aiohttp_jinja2
from aiohttp import web
from app.database import Transaction


@aiohttp_jinja2.template('index.html')
async def index(request):
    records = Transaction.select()
    return {'records': records}
