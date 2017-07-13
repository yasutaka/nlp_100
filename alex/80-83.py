# -*- coding: utf-8 -*-

import random
import codecs
import re
import pandas as pd
from pprint import pprint
import numpy as np
from gensim import corpora
from nltk.corpus import stopwords
import nltk
from sklearn.feature_extraction.text import CountVectorizer        

# ### 80
def tokenize(text):
    # remove non letters
    text = re.sub("[^a-zA-Z]", " ", text)
    tokens = nltk.word_tokenize(text)
    return tokens

ary = []
with open("enwiki.txt", 'rb') as myfile:
    head = [next(myfile) for x in xrange(1000)]
    for a in head:
        ar = tokenize(a)
        ary.append(ar)

with codecs.open('wiki_tokens.txt', 'w+') as f: pass
with codecs.open('wiki_tokens.txt', 'a+') as f:
    for c in ary:
        ## remove blank lines with lambda
        if (filter(lambda x:  not re.match(r'^\s*$', x), c)):
            f.write('\n')
            for cc in c:  
                f.write(cc + ' ')

### 81
countries = []
with open('country_list.txt', 'rb') as a:
    aa = a.readlines()
    for aaa in aa:
        countries.append(aaa.strip('\n'))

corrected_ary = []
with open('wiki_tokens.txt', 'rb') as t: 
    lines = t.readlines()
    for line in lines:
        #print line
        token_l = line.split()
        for token in token_l:
            if token in countries:
                #print token
                index = token_l.index(token)
                line = line.replace(token_l[index], countries[index]) ### dont work because different list lenght
                print line
                corrected_ary.append(line)
            else:
                corrected_ary.append(line)
print corrected_ary
print 'done'
