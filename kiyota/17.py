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

col1 = set() #セットを作成
with codecs.open('hightemp.txt','r','utf-8') as f0:
    dataset = f0.readlines()
    for row in dataset:
        col1.add(row.split()[0])  # setに要素を追加するにはadd

for word in sorted(col1):
    print(word)

# note
# pythonのsetは順序の保証がない。
# python 17.py
# ソートしたけど、UNIXの結果と並び順は不一致。アルファベットなら合致するが日本語はNG

# UNIX
# sortコマンド：行単位にキャラコード順に並び替える
# uniqコマンド：連続して重複した行を1つにまとめるコマンド。離れた行にも重複値がある場合、ソートが必要
# awkコマンド：行単位でデータファイルを様々に加工する
#   $ awk '{print $1}' "C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\hightemp.txt" | sort | uniq
