
from aws_config import settings
import redis

r = redis.Redis(
    host=settings.aws_elastic_cache_host,
    port=settings.aws_elastic_cache_port)

if r.ping():
    print("Connected to redis")