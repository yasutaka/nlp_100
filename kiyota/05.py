'''
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，
"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ

単語n-gram:隣り合うn個の単語を一塊として考える
文字gram：隣り合うn個の文字を一塊として考える
'''
# coding: utf-8

def do_ngram(ori,mode,num):
    if mode == "word":   #単語bi-gram
        str = []
        str = ori.split()
    elif mode == "char":   #文字bi-gram
        str = ""
        str = ori.replace(" ","")

    i = 0
    n = num
    ngram = []
    while i < len(str)-1:   #2個ずつ取り出して配列に入れたい
        ngram.append(str[i:n])

        i += 1
        n +=1

    print (ngram)


# ここから呼ぶ
ori_sentence =  "I am an NLPer"
# 単語bi-gram
do_ngram(ori_sentence,"word",2)
# 文字bi-gram
do_ngram(ori_sentence,"char",2)
