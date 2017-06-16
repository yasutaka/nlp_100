"""
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
  ・1行に1記事の情報がJSON形式で格納される
  ・各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，
  　そのオブジェクトがJSON形式で書き出される
  ・ファイル全体はgzipで圧縮される

  23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""

# note
# セクション名は2個以上つづく=で囲まれた文字。=の数-1がレベルに相応
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

# セクション名を取得
for line in p:
    s = re.search("\=\=+(.*?)\=\=+",line)
    
    if s is not None:
        # print(s.group(0))
        print(s.group(1),(len(s.group(0))-len(s.group(1)))//2)
