"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""
# -*- coding: utf-8 -*-

from common_function import do_mecab
import codecs

def get_nouns(data):
    nouns = []
    i = 0
    while i < len(data):
        sentence = data[i]
        j = 0
        noun = []
        while j < len(sentence):
            #print(sentence[j]["pos"])
            if sentence[j]["pos"] == "名詞":
                noun.append(sentence[j]["surface"])
            else:
                if len(noun) >= 2: #名詞が2つ以上続いているか？
                    nouns.append(''.join(noun))
                noun = []
            # 文章の最後が名詞だと上のelse通らないのでもう一回書く。。。
            if len(noun) >= 2:
                nouns.append(''.join(noun))
                noun = []
            j += 1
        i += 1
    #print(nouns)
    return nouns

def create_file(txtdata):
    with codecs.open('35-output.txt','w','utf-8') as f:
        f.write(str(txtdata))

list_d = do_mecab('neko.txt.mecab')
txt = get_nouns(list_d)
create_file(txt)

"""
list_d = [] #文書のリスト

def do_mecab(textfile):
    import codecs
    import copy
    list_s = [] #文章単位のリスト

    with codecs.open(textfile, 'r', 'utf-8') as f:
        for line in f:
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

do_mecab('test-neko.txt.mecab')
"""
