search_query=input('Enter Your Search Query: ')

import pymongo
from pymongo import MongoClient
connection = MongoClient()
connection.database_names()
db = connection.test1


for x in search_query.split():
    text=db.index.find_one({'text':x})
    print(text)
