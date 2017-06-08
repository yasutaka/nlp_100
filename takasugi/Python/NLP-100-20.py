import sys
import re
import json

argvs = sys.argv

#
#

file_path = argvs[1]
print(file_path)

f = open(file_path, "r")
data = list()

for l in f:
    json_obj = json.loads(l)
    data.append(json_obj)

#print(data)

for idx in range(0,len(data)):
#    print(data[idx]["title"])
    if data[idx]["title"] == u"イギリス":
        print(data[idx]['text'])
        break


    
