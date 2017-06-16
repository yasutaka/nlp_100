"""
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
  ・1行に1記事の情報がJSON形式で格納される
  ・各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，
  　そのオブジェクトがJSON形式で書き出される
  ・ファイル全体はgzipで圧縮される

  26. 強調マークアップの除去
  25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
  （弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．

　**wiki** 各種強調は、2～5個の'でくくられている
  弱い強調：他との区別（斜体）	''他との区別''	他との区別
  強調：強調（太字）	'''強調'''	強調
  強い強調：斜体と強調	'''''斜体と強調'''''
"""
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
            dic[s2.group(1)] = re.sub("'{2,5}'","",s3.group(1))
            #dic[s2.group(1)] = s3.group(0)
        else:
            #dic["公式国名"].append(s3.group(0))
            dic["公式国名"].append(re.sub("'{2,5}'","",s3.group(0)))
    else: #公式国名のvalue
        if s3 is not None:
            #dic["公式国名"].append(s3.group(0))
            dic["公式国名"].append(re.sub("'{2,5}'","",s3.group(0)))

print(dic)
