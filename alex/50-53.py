# -*- coding: utf-8 -*-
import re
from nltk.stem import *
from nltk.tokenize import TweetTokenizer
from collections import defaultdict

## N 50
doc_file = []
with open('nlp.txt', 'r') as f:
    for l in f:
        l = l.strip('\n')
        l = re.sub(re.escape('.'),'\n', l)
        l = re.sub(re.escape(';'),'\n', l)
        l = re.sub(re.escape('?'),'\n', l)
        l = re.sub(re.escape('!'),'\n', l)
        doc_file.append(l)
for x in doc_file:
    print x

#### cleaning array for N51+
doc_file = []
with open('nlp.txt', 'r') as f:
    for l in f:
        l = re.sub(re.escape('('),'', l)
        l = re.sub(re.escape(')'),'', l)
        doc_file.append(l.strip('\n'))
print doc_file

#remove common words and tokenize N. 53
stoplist = set('for a of the and to or in'.split())
for line in doc_file:
    texts = [word for word in line.lower().split() if word not in stoplist]
print [t for t in texts]

### stemming N.52
stemmer = porter.PorterStemmer()
s = [stemmer.stem(p) for p in texts]
print s

