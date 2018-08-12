import os

### REQUIRED FIELDS ###########################################################

TELEGRAM_BOT_TOKEN = ''
CHAT_ID = ''
TELEGRAM_API_ID = ''
TELEGRAM_API_HASH = ''

###############################################################################

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DEFAULT_DATE_FORMAT = '%d/%m/%y'
DEFAULT_TIME_FORMAT = '%H:%M'
DEFAULT_DATETIME_FORMAT = '{} {}'.format(DEFAULT_TIME_FORMAT,
                                         DEFAULT_DATE_FORMAT)

DEBUG = False

POLL_PRICE_PERIOD = 30 * MINUTE
CHECK_TRANSACTIONS_PERIOD = 15 * MINUTE
NOTIFICATIONS_ENABLED = True
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
APP_DIR = os.path.join(PROJECT_ROOT, 'app')
TEMPLATES_DIR = os.path.join(APP_DIR, 'templates')
DB_PATH = os.path.join(PROJECT_ROOT, 'database.sqlite')
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
