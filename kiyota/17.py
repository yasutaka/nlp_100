"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
→重複のない値？
"""

# -*- coding: utf-8 -*-
import codecs

with codecs.open('hightemp.txt','r','utf-8') as f0:
    dataset = f0.readlines()

with codecs.open('17-uniq.txt','w','utf-8') as f1:
    for row in dataset:
        word = row.split()
        f1.write(word[0] + '\n')

# note
# pythonのsetは順序の保証がない。
# python 17.py

# UNIX
# sortコマンド：行単位にキャラコード順に並び替える
# uniqコマンド：連続して重複した行を1つにまとめるコマンド。離れた行にも重複値がある場合、ソートが必要
#   $ sort "C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\17-uniq.txt" | uniq
