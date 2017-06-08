import sys
import re

argvs = sys.argv

#
#

file_path = argvs[1]
print(file_path)

f = open(file_path, "r")
data = dict()
for line in f:
    tmp = line.split("\t")
#    print(tmp, end='' )
    c = tmp[0]
    for idx in range(0, len(c)):
        if c[idx] in data.keys():
            data[c[idx]] += 1
        else:
            data[c[idx]] = 1


print(data)



    
