#!/usr/bin/env python3
'''Hello world pls
'''
import pymongo


def schools_by_topic(mongo_collection, topic):
    '''Hello pls pls pls
    '''
    return mongo_collection.find({'topics':{'$all':[topic]}})

