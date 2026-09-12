#!/usr/bin/env python3
"""Module that lists all documents"""


def list_all(mongo_collection):
    """Lists all documents"""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
