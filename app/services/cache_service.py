import redis


class RedisCache:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

    def set(self, key, value, ttl=None):
        """
        Setting the key and value within the redis cache
        """
        if ttl:
            self.redis.setex(key, ttl, value)
        else:
            self.redis.set(key, value)

    def get(self, key):
        """
        Get a value by key from Redis.
        """
        return self.redis.get(key)

    def delete(self, key):
        """
        Delete a key from Redis.
        """
        return self.redis.delete(key)
