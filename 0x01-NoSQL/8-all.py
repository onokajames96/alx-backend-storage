#!/usr/bin/env python3
"""
Python function that lists all documents in a collection.
"""


def list_all(mongo_collection):
    """
    Returns an Empty list if no document in the collection
    """
    return mongo_collection.find()
