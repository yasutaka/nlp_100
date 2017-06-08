import sys
import re

argvs = sys.argv

file_path = argvs[1]
print(file_path)

f = open(file_path, "r")
head = list()
for line in f:
    head.append(line[0])
#    print(line[0], end='')

print("Orginal: ", end='')
print(head)

ret = sorted(set(head), key=head.index)

print("After: ", end="")
print(ret)

#CLI
#cut -c 1 ../hightemp.txt | sort | uniq


