# -*- coding: utf-8 -*-
"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．

pyton2.7で実行
"""
import xml.etree.ElementTree as ET
import codecs

fname_parsed = 'nlp.txt.xml'
out_file = "output-54.txt"

# xmlファイルの読み込み
tree = ET.parse(fname_parsed)
root = tree.getroot()

output = ""
# word,lemma,POSの値を取得
for data in root.iter('token'):
	word = data.find(".//word").text
	lemma = data.find(".//lemma").text
	pos = data.find(".//POS").text
	#print(word,lemma,pos)
	#break
	output = output + word + '\t' + lemma + '\t' + pos + '\n'

with codecs.open(out_file,'w','utf-8') as f:
	f.write(output)
