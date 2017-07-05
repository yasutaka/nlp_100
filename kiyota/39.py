"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

# -*- coding: utf-8 -*-

from common_function import do_mecab
import collections
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname=r'C:\Windows\Fonts\ipaexg.ttf', size=14)

#list_d = do_mecab('test-neko.txt.mecab')
list_d = do_mecab('neko.txt.mecab')

word_all = [] #文章中の単語（表層）リスト
for line_s in list_d:
    word_s = [] # 1文中の単語（表層）リスト
    for line_w in line_s:
        word_s.append(line_w["surface"])
    word_all = word_all + word_s
count = collections.Counter(word_all).most_common()
#print(count)

rank = list(range(1, len(count) + 1))  # 同じ頻度の単語はとりあえず無視。余力あったら考える
#print(rank)

left = [] #x軸の値の位置
#data_x = [] #x軸の値：順位
data_y = [] #y軸の値：出現回数
i = 0

for data in count:
    #data_x.append(data[0])
    data_y.append(data[1])
    i += 1
plt.plot(rank,data_y,'bo') #x:順位、y:出現回数

# 対数グラフ
plt.xscale('log')
plt.yscale('log')

# グラフのタイトル、ラベル指定
plt.title("39. Zipfの法則", fontproperties=fp)
plt.xlabel('出現度順位', fontproperties=fp)
plt.ylabel('出現頻度', fontproperties=fp)
plt.grid(which="both")

plt.show()
