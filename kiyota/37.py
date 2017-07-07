"""
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

http://pythondatascience.plavox.info/matplotlib/%E6%A3%92%E3%82%B0%E3%83%A9%E3%83%95
"""
# -*- coding: utf-8 -*-

from common_function import do_mecab
import collections
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname=r'C:\Windows\Fonts\ipaexg.ttf', size=14)

list_d = do_mecab('test-neko.txt.mecab')
#list_d = do_mecab('neko.txt.mecab')

word_all = [] #文章中の単語（表層）リスト
for line_s in list_d:
    word_s = [] # 1文中の単語（表層）リスト
    for line_w in line_s:
        word_s.append(line_w["surface"])
    word_all = word_all + word_s
count = collections.Counter(word_all).most_common(10)
#print(collections.Counter(word_all).most_common(10))  #most_commonで並び替え

#print(count)

left = [] #x軸の値の位置
data_x = [] #x軸の値
data_y = [] #y軸の値
i = 0

for data in count:
    data_x.append(data[0])
    data_y.append(data[1])
    i += 1

#print(data_x)
#print(data_y)

left = np.arange(len(data_x))
#print(left)

plt.bar(left, data_y,align='center')
plt.xticks(left,data_x,fontproperties=fp) #値の書き換え
plt.show()

"""
data = [1,2,3]
left = data
height = [10,20,30]

plt.bar(left, height, align='center')
plt.xticks(left, ['東京','Osaka','Nagoya'],fontproperties=fp) #値の書き換え
plt.show() #でた～　showしないとでないのか。
"""
