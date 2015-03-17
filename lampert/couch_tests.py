from __future__ import absolute_import
import requests
from lampert.result import Result

def read(database, params, id):

    resp = requests.get(database, params=params)
    return Result(
        database=database,
        params=params,
        elapsed=resp.elapsed,
        test='read'
    )

def all_docs(database, params):
    resp = requests.get("{database}/_all_docs".format(database=database), params=params)
    return Result(
        database=database,
        params=params,
        elapsed=resp.elapsed,
        test='all_docs'
    )
