import os
from functools import partial

from aiohttp import web

import config
from app.app import configure_app


def run():
    uprint = partial(print, flush=True)
    port = int(os.environ.get('PORT', config.DEFAULT_RUN_PORT))
    app = configure_app()
    web.run_app(app, print=uprint, host=config.DEFAULT_RUN_HOST, port=port)


if __name__ == '__main__':
    run()
