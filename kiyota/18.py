"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

→「逆順」＝降順？
"""

# -*- coding: utf-8 -*-
import codecs

col1 = []
with codecs.open('hightemp.txt','r','utf-8') as f0:
    dataset = f0.readlines()
    for row in dataset:
        col1.append(row.split()[2])

for word in sorted(col1,reverse=True):
    print(word)

# note
# 実行コマンド
# python 18.py

# UNIX
# sortコマンドのオプションで　-grを指定
#   $ awk '{print $3}' "C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\hightemp.txt" | sort -gr
