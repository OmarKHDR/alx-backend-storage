#!/usr/bin/env python3
'''This docs is fucked up
'''
import pymongo


def insert_school(mongo_collection, **kwargs):
    '''Keyword  is  consistentciotrtrogjreg
    '''
    id = mongo_collection.insert_one(kwargs).inserted_id
    return id
