'''
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを
調べよ．
'''

# importでエラーになる・・・
#import 05
#x = set(05.do_ngram("paraparaparadise","char",2))


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
    return ngram


# 集合型にする　※値は重複して持たない
x = set(do_ngram("paraparaparadise","char",2))
print(x)
y = set(do_ngram("paragraph","char",2))
print(y)

# 和集合
print(x|y)
# 積集合
print(x&y)
# 差集合
print(x-y) #xの差集合
print(y-x) #yの差集合

print("se" in x)
print("se" in y)
