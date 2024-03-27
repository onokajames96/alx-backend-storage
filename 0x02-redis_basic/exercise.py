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
