#
# -*- coding: utf-8 -*-

import random


def scramble(str):
    if len(str) < 5:
        return str
    s_list = list(str)

    head_chr = s_list.pop(0)
    tail_chr = s_list.pop()

    random.shuffle(s_list)

    s_list.insert(0, head_chr)
    s_list.append(tail_chr)

    return ''.join(s_list)


a = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

a_list = a.split(' ')
b_list = map(lambda n: scramble(n), a_list)

print "Before:"
print a
print "After:"
print ' '.join(b_list)

