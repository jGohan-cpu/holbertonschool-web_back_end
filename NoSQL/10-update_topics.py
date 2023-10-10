#!/usr/bin/env python3
"""Script that change all topics of a school
document based on the name"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Changes all topics"""

    query: dict = {"name": name}

    mongo_collection.update_many(query, {"$set": {"topics": topics}})
