# author: alex
import re
from natto import MeCab
import csv

# 31 + 32
with open("verbs.txt", "w+"): pass
text = open("neko.txt","r+")
res_file = open("verbs.txt", "a+")
reader = text.readlines()
for line in reader:
    with MeCab('-F%f[0],%f[6]') as nm:
        for n in nm.parse(line, as_nodes=True):
            if not n.is_eos() and n.is_nor():
                klass, word = n.feature.split(',', 1)
                if klass in ['動詞']: #['名詞', '形容詞', '形容動詞','動詞']:
                    print word
                    res_file.write(word + ' ')
                    res_file.write('\n')
text.close()
res_file.close()


# 31 + 33
with open("neko_hen.txt", "w+"): pass
text = open("neko.txt","r+")
res_file = open("neko_hen.txt", "a+")
reader = text.readlines()
for line in reader:
    with MeCab('-F%f[1],%f[6]') as nm:
        for n in nm.parse(line, as_nodes=True):
            if not n.is_eos() and n.is_nor():
                klass, word = n.feature.split(',', 1)
                if klass in ['サ変接続']: #['名詞', '形容詞', '形容動詞','動詞']:
                    print word
                    res_file.write(word + ' ')
                    res_file.write('\n')
text.close()
res_file.close()




