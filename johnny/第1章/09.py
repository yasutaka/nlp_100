from random import randint

input_string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def typoglycemia(input_string):
    split_array = input_string.split(" ")
    preprocessed_array = []
    for value in split_array:
        if len(value) > 4:
            char_list = list(value)
            first_letter = char_list.pop(0)
            end_letter = char_list.pop()
            random_values = []
            random_values.append(first_letter)
            i = len(char_list)
            while i > 0:
                character = char_list.pop(randint(0, i-1))
                random_values.append(character)
                i -= 1
            random_values.append(end_letter)
            preprocessed_array.append("".join(random_values))
        else: preprocessed_array.append(value)
    return " ".join(preprocessed_array)

print typoglycemia(input_string)

    
