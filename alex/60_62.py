# -*- coding: utf-8 -*-

import redis
import json
import codecs

db = redis.Redis(host='localhost', port=6379, db=0)

## 60
with codecs.open('artist.json', 'r', 'utf_8') as json_data:
    for line in json_data:
        jsonData = json.loads(line)
        if "name" in jsonData and "area" in jsonData:
            db.set(jsonData["name"], jsonData["area"])

## 61
name = "Queen"
area = db.get(name)
print(name,area)

## 62
area = "Japan"
name = db.get(area)
print(name,area)
