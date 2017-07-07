"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""
# -*- coding: utf-8 -*-
import codecs

def do_mecab(textfile):
    import codecs
    import copy
    list_s = [] #文章単位のリスト
    list_d = [] #文書のリスト
    # load data
    with codecs.open(textfile, 'r', 'utf-8') as f:
        for line in f:
            #sys.stdout.write(str(line))
            morpheme = line.split("\t") # 表層形とその他に分離
            if morpheme[0] != "　" and len(morpheme) != 1: # 空白とEOSは除外
                element = morpheme[1].split(",")
                dic = {"surface":morpheme[0],"base":element[6],"pos":element[0],"pos1":element[1]}
                list_s.append(dic)
            else:
                if len(list_s) != 0:
                    list_d.append(copy.deepcopy(list_s))
                    list_s.clear()
        #print(list_d)
        return list_d

def verb_s(mecabify):
    #mecabify = do_mecab('test-neko.txt.mecab')
    verbwords = ""
    i = 0
    while i < len(mecabify):
        sentence = mecabify[i]
        j = 0
        while j < len(sentence):
            word = sentence[j]
            if word["pos"] == "動詞":
                verbwords = verbwords + word["surface"] + '\n'
                #print(word["surface"])
            j += 1
        i += 1
    #print(verbwords)
    return verbwords

def create_file(data):
    with codecs.open('31-output.txt','w','utf-8') as f:
        f.write(data)

#data = verb_s(do_mecab('test-neko.txt.mecab'))
data = verb_s(do_mecab('neko.txt.mecab'))
create_file(data)
