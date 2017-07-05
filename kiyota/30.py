"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）を
キーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""
# -*- coding: utf-8 -*-

import codecs
#import sys
import copy

list_s = [] #文章単位のリスト
list_d = [] #文書のリスト

# load data
#with codecs.open('test-neko.txt.mecab', 'r', 'utf-8') as f:
with codecs.open('neko.txt.mecab', 'r', 'utf-8') as f:

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
            #print(len(list_s))
    #print(list_d)

with codecs.open('output-30.txt', 'w', 'utf-8') as f0:
    f0.write(str(list_d))
