"""
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
  ・1行に1記事の情報がJSON形式で格納される
  ・各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，
  　そのオブジェクトがJSON形式で書き出される
  ・ファイル全体はgzipで圧縮される

以下の処理を行うプログラムを作成せよ．
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

# note
# pythonはJSONデータを読み込むと辞書にする。
# →jawiki-countryは1行ごとにJSON形式になっているので、1行ずつ読んで辞書のデータにする？

import codecs
import json

data = []
with codecs.open('jawiki-country.json', 'r','utf-8') as f:
    """
    jsonfile = f.readlines() #1行ごとに全部よむ
    for row in jsonfile:
        jsonData.append(row)
        # print(jsonData)
    """
    for row in f:
        jsonData = json.loads(row) # dic型
        if jsonData["title"] == "イギリス":
            data.append(jsonData["text"])
        jsonData.clear

    #print(data)
with codecs.open('output_jsondata2','w','utf-8')as f1:
    #f1.writelines(data)
    json.dump(data, f1, sort_keys = True, indent = 4,ensure_ascii=False)

#print(json.dumps(jsonData,sort_keys = True, indent = 4,ensure_ascii=False))
