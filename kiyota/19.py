"""
hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
----------------------------------------------------------
dictモジュール？collectionsモジュール？
dictモジュール：
    マップ型（ハッシュみたいなもん？）。要素間に順序はなくインデックスは使えない。
    各要素にはキー（識別子）を値と合わせて登録して使う　→　値とキーはペア。値はなんでもOK、キーは制約あり（＝変更不可）。
collectionsモジュール：
    コンテナデータ型
    counterクラスがある（要素を辞書のキーとして保存し、そのカウントを辞書の値として保存する、
    順序付けされていないコレクション）。便利そうなので今回使ってみる。
"""
import codecs
from collections import Counter

col1 = []
with codecs.open('hightemp.txt','r','utf-8') as f0:
    dataset = f0.readlines()
    for row in dataset:
        col1.append(row.split()[0])

cnt = Counter()
for word in col1:
    cnt[word] += 1

print(cnt.most_common())


# unix
# cutコマンド：タブ区切りでフィールドを選択して出力する、または各行の中の一部を範囲指定して出力するコマンド。
# 1列目をcutして、uniqでカウントする
#   cut -f1 "C:\Users\riekok.ZIPANGU\Documents\nlp_100\kiyota\Python\hightemp.txt" | sort | uniq -c | sort -gr
