"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．
"""

# -*- coding: utf-8 -*-
import sys
import codecs
argvs = sys.argv #コマンドライン引数：分割数
n = int(argvs[1])

with codecs.open('hightemp.txt','r','utf-8') as f0:
    dataset = f0.readlines()

# 出力するファイルの数を設定
if len(dataset)%n == 0:
    filenum = len(dataset)//n
else:
    filenum = len(dataset)//n +1

i = 0
while i < filenum:
    with codecs.open('split'+str(i+1)+'.txt','w','utf-8') as f1:
        f1.writelines(dataset[(0+n*i):(0+n*i+n)])
    i += 1

# note
# リストのスリットは、終り位置がリストの長さを越えていてもエラーにならず返す模様。

# UNIX
# splitコマンド：ファイルを分割する バイト単位か行単位か指定できる。
# $ split -l 8 "C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\hightemp.txt"
