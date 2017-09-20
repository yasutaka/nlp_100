# -*- coding:utf-8 -*-

def cipher(string):
    encoding = ""
    for character in string:
        #range 97 -> 123 = a-z
        if 97 <= ord(character) <= 123:
            #encode 219 - character number
            encoding +=chr(219-ord(character))
        else:
            encoding += character
    return encoding

input_value = "Hello World"
print cipher(input_value)
print cipher(cipher(input_value))
