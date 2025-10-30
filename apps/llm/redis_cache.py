import redis
from django.conf import settings

REDIS_HOST = settings.REDIS_HOST
REDIS_PORT = settings.REDIS_PORT
REDIS_USERNAME = settings.REDIS_USERNAME
REDIS_PASSWORD = settings.REDIS_PASSWORD

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    username=REDIS_USERNAME,
    password=REDIS_PASSWORD,
    decode_responses=True
)
