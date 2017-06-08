import sys
import re

argvs = sys.argv

file_path = argvs[1]
print(file_path)

f = open(file_path, "r")
line_num = 0
p = re.compile("\t") #¥t

for line in f:
#    print(line, end=" ")
    print(p.sub(' ', line), end='' )
    line_num = line_num + 1
