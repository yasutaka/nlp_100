import sys
import re

argvs = sys.argv

file_path = argvs[1]
print(file_path)

f = open(file_path, "r")
data = dict()
for line in f:
    tmp = line.split("\t")
    print(tmp, end='' )
    data[line] = float(tmp[2])


print(data)
vs = sorted(set(data.values()))
print(sorted(vs))

for v in sorted(vs):
    for k in data.keys():
        if v == data[k]:
            print("{}: {}".format(v, k))


