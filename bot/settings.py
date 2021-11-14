import os
# Telegram bot token
API_TOKEN = os.environ.get('API_TOKEN')
# Telegram id for admin User
ADMIN_ID = os.environ.get('ADMIN_ID')


try:
    from local_settings import *
except ImportError:
    pass
