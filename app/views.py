import aiohttp_jinja2
from aiohttp import web


@aiohttp_jinja2.template('index.html')
async def index(request):
    records = [
        {'date': '08/08/18', 'user': 'Misha', 'amount': 500, 'rate': 6300, 'closed': False},
        {'date': '08/08/18', 'user': 'Misha', 'amount': 600, 'rate': 6300, 'closed': False},
        {'date': '08/08/18', 'user': 'Misha', 'amount': 700, 'rate': 6300, 'closed': False},
        {'date': '08/08/18', 'user': 'Misha', 'amount': 800, 'rate': 6300, 'closed': False},
    ]
    return {'records': records}
