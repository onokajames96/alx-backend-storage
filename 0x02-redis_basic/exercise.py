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
