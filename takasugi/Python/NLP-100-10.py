import sys
import subprocess

argvs = sys.argv

file_path = argvs[1]
print(file_path)

f = open(file_path, "r")
line_num = 0
for line in f:
    print(line, end=" ")
    line_num = line_num + 1


print("PYTHON: " + str(line_num))

ret = subprocess.call(["wc", file_path])


