#!/usr/bin/env python3
'''Docs very imp
'''
import pymongo


def top_students(mongo_collection):
    '''Top is Top ;>
    '''
    return mongo_collection.aggregate([
        {
            '$unwind': "$topics"
        },
        {
            '$group': {
                '_id': '$name',
                'averageScore': {
                    '$avg': "$topics.score"
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ])
