"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

# -*- coding: utf-8 -*-

import sys
import codecs
argvs = sys.argv #コマンド引数の最初[0]には実行ファイル名が入るので注意

with codecs.open(argvs[1],'br','utf-8') as text:
    data = text.read()
    print(data.replace("\t"," "))

# note
# python：ファイル操作時、withステートメントを使うと、withを抜けた時に自動的にcloseされる

# unix 確認
# sedコマンド：文字列の置換を行う  ※gをつけないと最初の1文字だけ置換する。
#   $ sed -e "s/\t/ /g" < "C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\hightemp.txt"
# trコマンド：文字の置換や削除などを行うコマンド。 「tr 変換対象の文字 変換文字 < 対象ファイル」
#   $ tr "\t" " " < "C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\hightemp.txt"
# expandコマンド：タブをスペースに変換する  -tで置き換える幅（スペースの数）を指定
#   $ expand -t 1 "C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\hightemp.txt"
