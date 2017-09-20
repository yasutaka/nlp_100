def ngram(input_string, n):
    prep_string = input_string.replace(" ", "")
    output = []
    for i in range(len(prep_string)):
        output.append(prep_string[i:i+n])
    return output

def set_diff_equal(x, y, z):
    output = {}
    output['logical-sum'] = set(x).union(y)
    output['logical-product'] = set(x).intersection(y)
    output['logical-difference'] = set(x).symmetric_difference(y)
    output['queried-value-shared'] = (z[0] in output['logical-product'])
    output['queried-value-in-x'] = (z[0] in x)
    output['queried-value-in-y'] = (z[0] in y)
    return output

output = set_diff_equal(ngram("paraparaparadise",2), ngram("paragraph",2), ["se"])
print output
