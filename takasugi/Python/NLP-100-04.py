#
# -*- coding: utf-8 -*-
import re

#

#
check_str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

first_list = [1,5,6,7,8,9,15,16,19]

word_list = filter(lambda a: len(a) != 0, re.split(r"[,¥. ]", check_str))

print  word_list
out = {}

for idx in range(0, len(word_list)):
    key = ""

    if idx + 1 in first_list:
        key =  word_list[idx][0]
    else:
        key = word_list[idx][0:2] 


    out[key] = idx + 1


print out

