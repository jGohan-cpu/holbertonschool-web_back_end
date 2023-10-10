#!/usr/bin/env python3
"""Script that inserts a new document"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Add the new document"""

    added_doc = mongo_collection.insert_one(kwargs)

    return added_doc.inserted_id
