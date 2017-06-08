#
# -*- coding: utf-8 -*-
import re

def n_gram(n, obj, type="word"):
    check_list = ""
    if type == "word":
        check_list = filter(lambda a: len(a) != 0, re.split(r"[,¥. ]", obj))
    elif type == "string":
        check_list = re.sub(r"[,¥. ]", '', obj)
    else:
        return false

    out = []
    print check_list

    for idx in range(0, len(check_list) - n + 1):
        out.append(check_list[idx:idx + n])

    return out

#
check_str01 = "paraparaparadise"
check_str02 = "paragraph"

x = set(n_gram(2, check_str01, "string"))
y = set(n_gram(2, check_str02, "string"))

print x
print y

print "Union"
print x | y

print "Product set"
p = x & y
print p

print "Deifference set"
print x - y


