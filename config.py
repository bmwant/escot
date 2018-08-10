import os


TELEGRAM_BOT_TOKEN = ''

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
POLL_PERIOD = 15 * MINUTE


DEFAULT_RUN_PORT = 8088


# Override values from config_local.py
try:
    import config_local
    for key, value in config_local.__dict__.items():
        if key.isupper() and key in globals():
            globals()[key] = value
except ImportError:
    pass

# Override values from environment
for key, value in globals().copy().items():
    if key.isupper() and key in os.environ:
        globals()[key] = os.environ[key]
