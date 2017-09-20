# -*- coding: utf8 -*-
def modular(string):
    i=0
    result = ""
    for i in range(0, len(string)):
        if i % 2 != 0:
            result += string[i]
    return result

print modular(u"パタトクカシーー")
