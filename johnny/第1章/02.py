# -*- coding: utf8 -*-
string1 = u"パトカー"
string2 = u"タクシー"

def head_only(input_1, input_2):
    output = u""
    i = 0
    for i in range(0, len(input_1)):
        output += input_1[i] + input_2[i]
    return output
                                  

print head_only(string1, string2)
