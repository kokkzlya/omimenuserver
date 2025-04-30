import inject
import redis

class AuthRepository:
    redis_client = inject.attr(redis.Redis)

    def save_token(self, key: str, value: str):
        self.redis_client.set(key, value, ex=3600 * 3)  # Token expires in 3 hour

    def get_token(self, key: str):
        return self.redis_client.get(key)

    def delete_token(self, key: str):
        self.redis_client.delete(key)
