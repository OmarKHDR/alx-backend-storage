#!/usr/bin/env python3
'''This is my docs
'''
import pymongo


def update_topics(mongo_collection, name, topics):
    '''Por fa Vour
    '''
    mongo_collection.update_many({'name':name}, {'$set':{'topics':topics}})
    