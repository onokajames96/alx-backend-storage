#!/usr/bin/env python3
"""
A  function that changes all topics of a school document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Defining function that Changes school topic
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
