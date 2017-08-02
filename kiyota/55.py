# -*- coding: utf-8 -*-
"""
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．

pyton2.7で実行
"""
import xml.etree.ElementTree as ET
import codecs

fname_parsed = 'nlp.txt.xml'
out_file = "output-55.txt"

# xmlファイルの読み込み
tree = ET.parse(fname_parsed)
root = tree.getroot()

word = ""
# 人名の取得
for data in root.iter('token'):
	if data.find(".//NER").text == "PERSON":
		word = word + data.find(".//word").text + '\n'
		#print(word)
		#break

with codecs.open(out_file,'w','utf-8') as f:
	f.write(word)
