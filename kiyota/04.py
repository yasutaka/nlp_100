'''
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also
Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8,
9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列
から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
'''

# coding: utf-8

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might \
Also Sign Peace Security Clause. Arthur King Can."

words_list = []
words_list = str.split()
#print(words_list)

dic = {}
w = ""
n = 1
for word in words_list:
    if n % 2 != 0:  #奇数
        w = word[0:1]
        dic[w] = n
        n = n + 1
    else: #偶数
        w = word[0:2]
        dic[w] = n
        n = n + 1
print(dic)
