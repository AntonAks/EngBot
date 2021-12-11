import os
# Telegram bot token
API_TOKEN = os.environ.get('API_TOKEN')
# Telegram id for admin User
ADMIN_ID = os.environ.get('ADMIN_ID')
# url for bd connections
DB = os.environ.get('DB')

AWS_S3_BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

try:
    from local_settings import *
except ImportError:
    pass
