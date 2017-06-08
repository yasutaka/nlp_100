import sys

argvs = sys.argv

file_path = argvs[1]
div_n = argvs[2]

print(file_path)
print(div_n)

f = open(file_path, "r")
line_num = 0
for line in f:
#    print(line, end=" ")
    line_num = line_num + 1

print(line_num)

f.close

f = open(file_path, "r")

file_n = 0
new_file_flg = True
c_line_num = 0
for line in f:
    if new_file_flg:
        out_f = open(file_path + str(file_n), "w")
        new_file_flg = False
        
    out_f.write(line, end='')
    c_line_num += 1

        
    if c_line_num == div_n:
         out_f.close
         new_file_fag = True
         c_line_num = 0
            

        

