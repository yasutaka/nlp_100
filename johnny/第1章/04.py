# -*- coding: utf8 -*-

input_str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

def dict_out(input_string):
    preprocessed_string = input_string.replace(".", "")
    preprocessed_string = preprocessed_string.split(" ")
    first_char_array = [1,5,6,7,8,9,15,16,19]
    output = []
    for word in preprocessed_string:
        if preprocessed_string.index(word) in first_char_array:
            tmp = { word[:1]: { "word-index": preprocessed_string.index(word)}}
        else:
            tmp ={ word[:2]: { "word-index": preprocessed_string.index(word)}}
        output.append(tmp)
    return output

print dict_out(input_str)
                        
                   
