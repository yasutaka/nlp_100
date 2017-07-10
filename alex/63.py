# -*- coding: utf-8 -*-

import redis
import json
import codecs
from pprint import pprint
from ast import literal_eval

db = redis.Redis(host='localhost', port=6379, db=0)

# 63
with codecs.open('artist.json', 'r', 'utf_8') as json_data:
    for line in json_data:
        jsonData = json.loads(line)
        if "tags" in jsonData:
            #print(jsonData["name"],jsonData["tags"])
            tags = json.dumps(jsonData["tags"])
            db.set(jsonData["name"], tags)

name = "Queen"
tags = literal_eval(db.get(name))
print('Queen Tags: ' + '\n')
for tag in tags:
    print(tag["value"] +': '+ str(tag["count"]))
