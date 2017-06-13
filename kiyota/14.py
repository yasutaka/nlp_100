"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
"""
# -*- coding: utf-8 -*-
import sys
import codecs

argvs = sys.argv

def output_data(n):
    with codecs.open('head.txt','bw','utf-8')as f0:
        with codecs.open('hightemp.txt','br','utf-8') as f1:
            i = 1
            while i <= int(n):
                f0.write(f1.readline())
                i += 1

output_data(argvs[1])
# note
# コマンドラインの入力例
#   python　14.py 20

# UNIX
# headコマンド
#   $ head -n20 "C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\hightemp.txt"
