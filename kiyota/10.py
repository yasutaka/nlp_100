"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""
# -*- coding: utf-8 -*-
import sys
argvs = sys.argv #コマンド引数の最初[0]には実行ファイル名が入るので注意

input_file = open(argvs[1],'rb')

i = 0
for row in input_file:
    i += 1
print(i)

input_file.close()

# memo:コマンドラインでの指定時、ファイル名に''不要
# ex) python 10.py hightemp.txt

#UNIXコマンドの実行@Cygwin
# wc -l 'C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\highttemp.txt'
#結果
#24 'C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\highttemp.txt'

'''
def row_count(filename,mode):
    input_file = open(filename,mode)

    i = 0
    for row in input_file:
        i += 1
    print(i)

    input_file.close()

row_count('hightemp.txt','rb')
'''
