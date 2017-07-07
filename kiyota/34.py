"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""
# -*- coding: utf-8 -*-
import codecs
list_d = [] #文書のリスト

def do_mecab(textfile):
    import codecs
    import copy
    list_s = [] #文章単位のリスト
    #list_d = [] #文書のリスト
    # load data
    with codecs.open(textfile, 'r', 'utf-8') as f:
        for line in f:
            #sys.stdout.write(str(line))
            morpheme = line.split("\t") # 表層形とその他に分離
            #print(morpheme)
            if morpheme[0] != "　" and len(morpheme) != 1: # 空白とEOSは除外
                #print(morpheme)
                element = morpheme[1].split(",")
                dic = {"surface":morpheme[0],"base":element[6],"pos":element[0],"pos1":element[1]}
                list_s.append(dic)
                #list_s.append(copy.deepcopy(dic))
                #print(list_s)
            else:
                if len(list_s) != 0:
                    #print(list_s)
                    list_d.append(copy.deepcopy(list_s))
                    list_s.clear()
    return list_d

def get_nphrase():
    nphrase = ""
    i = 0
    while i < len(list_d):
        sentence = list_d[i]
        j = 0
        while j < len(sentence)-2:
            #print(sentence[j]["pos"] + sentence[j]["surface"] + sentence[j]["pos"])
            if sentence[j]["pos"] + sentence[j+1]["surface"] + sentence[j+2]["pos"] == "名詞の名詞":
                phrase = sentence[j]["surface"] + sentence[j+1]["surface"] + sentence[j+2]["surface"]
                nphrase = nphrase + phrase + '\n'
                #print(phrase)
            j += 1
        i += 1
    return nphrase

def create_file(data):
    with codecs.open('34-output.txt','w','utf-8') as f:
        f.write(data)

#do_mecab('test-neko.txt.mecab')
do_mecab('neko.txt.mecab')
txtdata = get_nphrase()
create_file(txtdata)
#print(list_d)
#print(list_d[1])
#print(list_d[1][0]["pos"])
