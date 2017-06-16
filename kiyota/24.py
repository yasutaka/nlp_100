"""
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
  ・1行に1記事の情報がJSON形式で格納される
  ・各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，
  　そのオブジェクトがJSON形式で書き出される
  ・ファイル全体はgzipで圧縮される

  24. ファイル参照の抽出
  記事から参照されているメディアファイルをすべて抜き出せ．
"""

#
import codecs
import json
import re

data = []   #dataには改行コードを含め、がっさり1つのtitleのデータが入る。
# イギリスの記事を取得
with codecs.open('jawiki-country.json', 'r','utf-8') as f:
    for line in f:
        jsonData = json.loads(line) # dic型
        if jsonData["title"] == "イギリス":
            data.append(jsonData["text"])
        jsonData.clear

# 改行コードで分離
for line in data:
    p = line.split("\n")  #1titleのデータを行に分ける。

for line in p:
    s1 = re.search("\[\[ファイル:(.*?)\|",line)
    s2 = re.search("\[\[File:(.*?)\|",line)
    if s1 is not None:
        print(s1.group(1))
    elif s2 is not None:
        print(s2.group(1))
    
