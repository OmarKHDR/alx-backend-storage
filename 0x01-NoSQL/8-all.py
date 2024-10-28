#!/usr/bin/env python3
'''This is the summary line
'''
import pymongo


def list_all(mongo_collection):
    '''This is docs sumarry list_all
    '''
    for i in mongo_collection.find():
        print(i)
