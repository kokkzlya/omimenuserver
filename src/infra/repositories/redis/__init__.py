import redis
from flask import Flask

def create_redis_client(app: Flask):
    """
    Create a Redis client.
    """
    return redis.Redis.from_url(app.config["REDIS_URL"], decode_responses=True)
