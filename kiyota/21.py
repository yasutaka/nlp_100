"""
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
  ・1行に1記事の情報がJSON形式で格納される
  ・各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，
  　そのオブジェクトがJSON形式で書き出される
  ・ファイル全体はgzipで圧縮される

21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""
import codecs
import json

data = []   #dataには改行コードを含め、がっさり1つのtitleのデータが入る。
with codecs.open('jawiki-country.json', 'r','utf-8') as f:
    for line in f:
        jsonData = json.loads(line) # dic型
        if jsonData["title"] == "イギリス":
            data.append(jsonData["text"])
        jsonData.clear

for line in data:
    p = line.split("\n")  #1つtitleのデータを行に分ける。
    #print(lines)
    #break

for line in p:
    if "Category" in line:
        print(line)

# pはもともとの文章の塊はわからなくなっているのでそこはイマイチ
