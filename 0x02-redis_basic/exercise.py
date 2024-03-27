#!/usr/bin/env python3
"""
Module
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """
    cache class
    """
    def __init__(self):
        """
        Initialization and setting up redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        stores data in the cache and returns the key.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) \
            -> Union[str, bytes, int, float, None]:
        """
        a get method that take a key
        """
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self: bytes) -> str:
        """
        parametrize Cache.get with the correct conversion function.
        """
        return self.decode("utf-8")

    def get_int(self, key: str) -> Union[int, None]:
        """
        parametrize Cache.get with the correct conversion function.
        """
        return self.get(key, fn=int)
