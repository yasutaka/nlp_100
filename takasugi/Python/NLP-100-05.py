#
# -*- coding: utf-8 -*-
import re

# reference: https://en.wikipedia.org/wiki/N-gram

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

print n_gram(3, "1 2 3 4 5a")

check_str = "I am an NLPer"

print "bi-gram for Char"
print n_gram(2, check_str, "string")

print "bi-gram for work"
print n_gram(2, check_str)


        


