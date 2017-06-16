"""
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
  ・1行に1記事の情報がJSON形式で格納される
  ・各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，
  　そのオブジェクトがJSON形式で書き出される
  ・ファイル全体はgzipで圧縮される

27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

**wiki** 内部リンクの表記　　普通の文字だけにする
[[記事名]]
[[記事名|表示文字]]
[[記事名#節名|表示文字]]
"""
import codecs
import json
import re

def remove_markup(str):
    str = re.sub(r"'{2,5}'",r"",str)
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2",str)
    return  str

data = []   #dataには改行コードを含め、がっさり1つのtitleのデータが入る。
# イギリスの記事を取得
with codecs.open('jawiki-country.json', 'r','utf-8') as f:
    for line in f:
        jsonData = json.loads(line) # dic型
        if jsonData["title"] == "イギリス":
            data.append(jsonData["text"])
        jsonData.clear

# 基礎情報の部分を抜出
for line in data:
    s1 = re.search("\{\{基礎情報 国\n(.*?)\n\}\}",line,re.DOTALL)
    #print(s1.group(1))

items = s1.group(1).split("\n")

dic = {}
dic["公式国名"] = []
for item in items:
    s2 = re.search("^\|(.*?) =",item) # key
    s3 = re.search("= (.*)|\{\{(.*?)>",item,re.DOTALL) # value

    if s2 is not None:
        if s2.group(1) != "公式国名":
            dic[s2.group(1)] = remove_markup(s3.group(0))
        else:
            dic["公式国名"].append(remove_markup(s3.group(0)))
    else: #公式国名のvalue
        if s3 is not None:
            dic["公式国名"].append(remove_markup(s3.group(0)))

print(dic)
