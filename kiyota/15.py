"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ．
"""
# -*- coding: utf-8 -*-
import sys
import codecs
argvs = sys.argv

def gettail(rownum):
    roaddata = []
    with codecs.open('hightemp.txt','r','utf-8') as f1:
        roaddata = list(f1.readlines())

    for row in roaddata[len(roaddata)-int(rownum):]:
        print(row.rstrip())

gettail(argvs[1])

# note
#   スライスのステップは指定インデックスから後ろに進む。ので、-1から前に3つとかはできない
# コマンドラインの入力
#   python 15.py 3

# UNIX
# tailコマンド：ファイルの末尾 N行を表示したり、ログファイルを監視してログに追記されたものを
# リアルタイム表示できる
#   $ tail -3  "C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\hightemp.txt"
