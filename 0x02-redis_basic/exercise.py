#!/usr/bin/env python3
"""
Module
"""
import redis
from uuid import uuid4
from functools import wraps
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

    @staticmethod    
    def count_calls(method: Callable) -> Callable:
        """
        Decorator that takes a single method Callable argument
        and returns a Callable.
        """
        @wraps(method)
        def invoker(self, *args, **kwargs) -> Any:
            """
            Invoking process
            """
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return invoker

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
