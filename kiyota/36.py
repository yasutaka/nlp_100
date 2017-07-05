"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""
# -*- coding: utf-8 -*-

from common_function import do_mecab
import collections
import codecs
from datetime import datetime

#list_d = do_mecab('test-neko.txt.mecab')
#print('start-mecab:' + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
list_d = do_mecab('neko.txt.mecab')
#print('end-mecab:' + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

#print('start-count:' + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
word_all = [] #文章中の単語（表層）リスト
for line_s in list_d:
    word_s = [] # 1文中の単語（表層）リスト
    for line_w in line_s:
        word_s.append(line_w["surface"])
    word_all = word_all + word_s

count = collections.Counter(word_all).most_common
#print(collections.Counter(word_all).most_common)  #most_commonで並び替え
#print('end-count:' + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

with codecs.open('output-36.txt', 'w','utf-8') as f:
    #print('start-output:' + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    f.write(str(count))
    #print('end-output:' + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

"""
start-mecab:2017/06/30 14:20:44
end-mecab:2017/06/30 14:20:48
start-count:2017/06/30 14:20:48
end-count:2017/06/30 14:21:28
start-output:2017/06/30 14:21:28
end-output:2017/06/30 14:21:28
"""
