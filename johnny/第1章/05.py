def ngram(input_string, n, by_word=None):
        if not by_word:
                prep_string = input_string.replace(" ", "")
                output = []
                for i in range(len(prep_string)):
                        output.append(prep_string[i:i+n])
                return output
        else:
                prep_string = input_string.split(" ")
                output = []
                for i in range(len(prep_string)):
                        if ((i+n-1) < len(prep_string)):
                                output.append((prep_string[i],(prep_string[i+n-1])))
                return output
		
input_string="I am an NLPer"
print ngram(input_string, 2, by_word=True)
print ngram(input_string, 2, by_word=False)
