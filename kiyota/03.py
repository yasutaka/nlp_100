# "Now I need a drink, alcoholic of course, after the heavy lectures involving
# quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から
# 出現順に並べたリストを作成せよ．

# coding: utf-8

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

str = str.replace(",","")
str = str.replace(".","")
str = str.split()

list = []

for word in str:
    list.append(len(word))

print(list)
