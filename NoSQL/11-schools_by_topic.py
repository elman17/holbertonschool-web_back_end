#!/usr/bin/env python3


def schools_by_topic(mongo_collection, topic):
    """Return the list of school having a specific topic"""
    if mongo_collection is None:
        return []
    return [doc for doc in mongo_collection.find({"topics": topic})]
