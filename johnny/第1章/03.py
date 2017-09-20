# -*- coding: utf8 -*-

input_string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

def sort_by_length(input_text, reverse_output):
    preprocessed_string = input_text.replace(".", "")
    preprocessed_string = preprocessed_string.replace(",", "")
    preprocessed_string = preprocessed_string.split(" ")
    preprocessed_string.sort(key=len, reverse=reverse_output)
    print preprocessed_string
    return preprocessed_string

sort_by_length(input_string, True)
        
