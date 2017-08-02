# -*- coding: utf-8 -*-
"""
57. 係り受け解析
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして
可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．

python2.7で実行
sentence単位に、dependenciesから、governorとdependentのTextをセットで取得
"""
import xml.etree.ElementTree as ET
import codecs
import pydot

#fname_parsed = 'test-nlp.txt_2013.xml'
fname_parsed = 'nlp.txt_2017.xml'

# xmlファイルの読み込み
tree = ET.parse(fname_parsed)
root = tree.getroot()

"""
for child in root:
	#print child[0][0][3].tag, child[0][0][3].attrib
	print child[0][0][3][0][0].text
	構造はわかったけどこうじゃない感すごい・・・
"""
# pydotのinputとなるリストを作成
sentences = []
dependencies = []
dep = []

skipwords = [".",","]
for sentence in root[0][0]:
	#print(sentence[3].tag,sentence[3].attrib)
	for dep in sentence[3]:
		#print(dep[0].text,dep[1].text)
		if dep[0].text not in skipwords and dep[1].text not in skipwords:
			dependencies.append([dep[0].text,dep[1].text])
			#print(dependencies)
			#break
	sentences.append(dependencies) #sentence単位にリストに格納
	dependencies = []
	#print(sentences)


# リスト取り出してpydotで描画 .と,を渡すとエラーがでる様子・・・
i = 0
while i < len(sentences):
	#print(sentences)
	edges = sentences[i]
	g=pydot.graph_from_edges(edges)
	g.write_jpeg('graph_from_edges_dot' + str(i) +'.jpg', prog='dot')
	i += 1
