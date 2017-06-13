"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキスト
ファイルを作成せよ．確認にはpasteコマンドを用いよ
"""
# -*- coding: utf-8 -*-
import codecs

# ファイル読み込み
with codecs.open('col1.txt','br','utf-8') as f1:
    data1 = f1.readlines()
with codecs.open('col2.txt','br','utf-8') as f2:
    data2 = f2.readlines()

with codecs.open('merge.txt','bw','utf-8') as f3:
    for col1,col2 in zip(data1,data2):
        f3.write("\t".join([col1.rstrip(),col2]))

# note
# UNIX
# pasteコマンド：複数のファイルを行単位に連結
#   $ paste "C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\col1.txt" "C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\col2.txt"
