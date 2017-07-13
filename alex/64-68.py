# -*- coding: utf-8 -*-

from pymongo import MongoClient, ASCENDING, DESCENDING
import json
import codecs
from pprint import pprint

client = MongoClient()
db = client["NLP"] 
db.artist
collection = db.artist 

# 64 - database making
with codecs.open('artist.json', 'r', 'utf_8') as json_data:

    ary = []
    for line in json_data:
        jsonData = json.loads(line)
        ary.append(jsonData) 
    collection.insert_many(ary)


collection.create_index([("name", ASCENDING)])
collection.create_index([("rating.value", ASCENDING)])
collection.create_index([("tags.value", ASCENDING)])
collection.create_index([("aliases.name", ASCENDING)])
# test
print(collection.find({'tags.value':'hard rock'}).count())
client.close()

# 65
for queen in collection.find({'name': 'Queen'}):
    print (queen)

# 66
print(collection.find({'area':'Japan'}).count())

# 67
name = "Queen"
alias = collection.find({"aliases.name": name})
if alias:
    for x in alias:
        print x
else:
    print ("No alias found")

## 68
counte = 0
for x in collection.find({'tags.value':'dance'}).sort('rating.count', DESCENDING):
    counte += 1
    print (x["name"])
    if (counte == 10):
        break

## 69




