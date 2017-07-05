"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
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

left = [] #x軸の値の位置
data_x = [] #x軸の値
data_y = [] #y軸の値
i = 0

for data in count:
    #print(data)
    data_x.append(data[0])
    data_y.append(data[1])
    i += 1

plt.hist(data_y,bins=20,range=(0,50))

# グラフのタイトル、ラベル指定
plt.title("38. ヒストグラム", fontproperties=fp)
plt.xlabel('出現頻度', fontproperties=fp)
plt.ylabel('単語の種類数', fontproperties=fp)

plt.show()
