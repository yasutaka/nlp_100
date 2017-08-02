# -*- coding: utf-8 -*-
"""
58. タプルの抽出
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．

述語: nsubj関係とdobj関係の子（dependant）を持つ単語
主語: 述語からnsubj関係にある子（dependent）
目的語: 述語からdobj関係にある子（dependent）
"""
import xml.etree.ElementTree as ET
import codecs

fname_parsed = 'nlp.txt_2013.xml'
out_file = "output-58.txt"

# xmlファイルの読み込み
tree = ET.parse(fname_parsed)
root = tree.getroot()

output = ""
for sentence in root[0][0]:
	#print(sentence[3].tag,sentence[3].attrib) #collapsed-dependencies

	pred_dic = {} #述語
	sub_dic = {} #主語
	obj_dic = {} #目的語
	for dep in sentence[3]:
		# 主語はnsubjのdependet、predはgovernor
		if dep.attrib["type"] == "nsubj":
			#print(dep[0].attrib,dep[0].text,dep[1].attrib,dep[1].text) #dep[0]がgovernor、dep[1]がdependent
			#print(dep[0].attrib["idx"]) #これをキーにしたい
			pred_dic[dep[0].attrib["idx"]] = dep[0].text
			sub_dic[dep[0].attrib["idx"]] = dep[1].text
		elif dep.attrib["type"] == "dobj":
			pred_dic[dep[0].attrib["idx"]] = dep[0].text
			obj_dic[dep[0].attrib["idx"]] = dep[1].text
	#print("pre",pred_dic,"sub",sub_dic,"obj",obj_dic)

	if len(pred_dic) != 0:
		for k in pred_dic.keys():
			if k in sub_dic and k in obj_dic:
				#「主語 述語 目的語」
				#print(sub_dic[k],pred_dic[k],obj_dic[k])
				output += sub_dic[k] + '\t' + pred_dic[k] + '\t' + obj_dic[k] + '\n'

#print(output)

with codecs.open(out_file,'w','utf-8') as f:
	f.write(output)
