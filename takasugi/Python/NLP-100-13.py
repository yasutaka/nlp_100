import sys
import re

argvs = sys.argv

file_path1 = argvs[1]
file_path2 = argvs[2]

print(file_path1)
print(file_path2)

f1 = open(file_path1, "r")
f2 = open(file_path2, "r")

list01 = []
for line in f1:
    list01.append(line.strip())

list02 = []
for line in f2:
    list02.append(line.strip())

for idx in range(0, len(list01)):
    print([list01[idx] + 'T' + list02[idx])
          

