'''
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序を
ランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば"I couldn't believe that I could actually understand what I
was reading : the phenomenal power of the human mind ."）を与え，その実行結果を
確認せよ．
'''

import random

text = "I couldn't believe that I could actually understand what I was \
reading : the phenomenal power of the human mind ."


words = []
words = text.split()


shuffled_word = [] #シャッフルする文字
shuffled_str = [] #シャッフル後の文

for word in words:
    if len(word) <= 4: #4文字以下はそのまま出力
        shuffled_str.append(word)
    else:
        shuffled_word = list(word[1:-1]) #並び替えの対象はリストにする。
        random.shuffle(shuffled_word)
        shuffled_str.append(word[0] + "".join(shuffled_word) + word[-1])

print(shuffled_str)
