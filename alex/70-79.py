# -*- coding: utf-8 -*-

import random
import codecs
import re
import pandas as pd
from pprint import pprint
import numpy as np
from nltk.corpus import stopwords
import nltk
from sklearn.feature_extraction.text import CountVectorizer        
from nltk.stem.porter import PorterStemmer
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
import matplotlib.pyplot as plt


## 70
feelings = []
with codecs.open('rt-polaritydata/rt-polaritydata/rt-polarity.pos', 'rb') as pos:
    p = pos.readlines()
    for pp in p:
        feelings.append(str(str('+1') + '\t' +pp))

with codecs.open('rt-polaritydata/rt-polaritydata/rt-polarity.neg', 'rb') as neg:
    p = neg.readlines()
    for pp in p:
        feelings.append(str(str('-1') + '\t' +pp))

random.shuffle(feelings)
with codecs.open('sentiment.txt', 'a+') as f:
    for line in feelings:
        f.write(line)



## 71 + 72
### making dataframe from sentiment file
df = pd.read_csv('sentiment.txt', header=None, delimiter="\t", quoting=3, nrows=100)
df.columns = ["sentiment","text"]
y = df['sentiment']
print df.shape
### stemming
stemmer = PorterStemmer()
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

##### tokenizing
def tokenize(text):
    # remove non letters
    text = re.sub("[^a-zA-Z]", " ", text)
    # tokenize
    tokens = nltk.word_tokenize(text)
    # stem
    stems = stem_tokens(tokens, stemmer)
    return stems


##### vectorizing
vectorizer = CountVectorizer(
    analyzer = 'word',
    tokenizer = tokenize,
    lowercase = True,
    stop_words = 'english',
    max_features = 85
)

corpus = vectorizer.fit_transform(
    df.text.tolist())

#### transform into np.array
corpus_nd = corpus.toarray()
#print corpus_nd.shape

### 75
# ##### define vocabulary for future reference
# vocab = vectorizer.get_feature_names()
# ### Sum up the counts of each vocabulary word
# dist = np.sum(corpus_nd, axis=0)
# ### For each, print the vocabulary word and the number of times it appears in the data set
# for tag, count in zip(vocab, dist):
#     print count, tag



## 76
X_train, X_test, y_train, y_test  = train_test_split(corpus_nd, df.sentiment, test_size=0.33)
print (X_train.shape, y_train.shape)
print (X_test.shape, y_test.shape)

## 73 + 74
#### logistic regression
log_model = LogisticRegression()
log_model = log_model.fit(X=X_train, y=y_train)

## 77 + 78
y_pred = log_model.predict(X_test)
print(classification_report(y_test, y_pred))

## 79
precision = dict()
recall = dict()
average_precision = dict()

false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
print thresholds
roc_auc = auc(false_positive_rate, true_positive_rate)


print 'gonna plot'
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate, true_positive_rate, 'b',
label='AUC = %0.2f'% roc_auc)
plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()