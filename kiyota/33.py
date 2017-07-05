"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""
# -*- coding: utf-8 -*-
list_d = [] #文書のリスト
import codecs

def do_mecab(textfile):
    #import codecs
    import copy
    list_s = [] #文章単位のリスト
    #list_d = [] #文書のリスト
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
    return list_d

def get_word2(mecabify,parse,element):
    nouns = ""
    i = 0
    while i < len(mecabify):
        sentence = mecabify[i]
        j = 0
        while j < len(sentence):
            word = sentence[j]
            if word["pos"] == parse and word["pos1"] =="サ変接続":
                #print(word[element])
                nouns = nouns + word[element] + '\n'
            j += 1
        i += 1
    #print(output)
    return nouns

def create_file(data):
    with codecs.open('33-output.txt','w','utf-8') as f:
        f.write(data)

do_mecab('neko.txt.mecab')
txtdata = get_word2(list_d,"名詞","surface")
create_file(txtdata)
