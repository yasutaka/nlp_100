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

ret = ''
for idx in range(0,len(data)):
#    print(data[idx]["title"])
    if data[idx]["title"] == u"イギリス":
        ret = data[idx]['text']
#        print(data[idx]['text'])
        break


lines = ret.split("\n")

for ll in lines:
    m = re.search('^\[\[Category:(.+)(\|.+|)\]\]', ll)
    print(m)
    if m:
        r = m.group(1)
        print(r.split('|')[0])
#        print(r)
