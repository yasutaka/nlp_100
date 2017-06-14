"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとして
ファイルに保存せよ．確認にはcutコマンドを用いよ．
"""
# -*- coding: utf-8 -*-
import sys
import codecs

argvs = sys.argv
col1words = []
col2words = []

def road_data(filename):
    with codecs.open(filename,'br','utf-8') as text:
        row = []
        for line in text:
            row = line.split()
            col1words.append(row[0])
            col2words.append(row[1])
            row.clear
    return(col1words)
    return(col2words)

def create_file(col,list):
    with codecs.open(col+'.txt','bw','utf-8') as f:
        i = 1

        for words in list:
            if i == len(list):
                f.write(words)
            else:
                f.write(words+'\n')
            i += 1

road_data(argvs[1])
create_file("col1",col1words)
create_file("col2",col2words)

# UNIX
# cutコマンド：テキストファイルの各行から指定した部分の文字列を切り出して表示
#   $ cut -f1 "C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\hightemp.txt"
#   $ cut -f2 "C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\hightemp.txt"
