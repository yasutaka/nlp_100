# -*- coding: utf-8 -*-

"""
59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．
入れ子になっている名詞句もすべて表示すること．
"""
import xml.etree.ElementTree as ET
import codecs
import re
import six

#fname_parsed = 'test-nlp.txt_2013_2.xml'
fname_parsed = 'test-nlp.txt_2013.xml'
out_file = "output-59.txt"

# xmlファイルの読み込み
tree = ET.parse(fname_parsed)
root = tree.getroot()

# parseタグの１文字ずつバラバラにしてリストにする
sentences = []
for sentence in root[0][0]:
	parse = re.sub(r'\)',r' )',sentence[1].text) # parseの取り出し
	#print (parse)
	parse = re.sub(r'\(',r'( ',parse)
	#print (parse)
	tokens = re.split(" ",parse) #バラバラ
	#print(tokens) #取れている
	sentences.append(tokens)
	#print(sentences)
	#print(len(sentences))


# ()の数で階層を判断。（で階層を＋１、）で−１、
output = ""
for parse in sentences: #parseは１文分のparse結果（バラバラ）
	n=0
	#NPwordlist = []
	for word in parse:
		RBcounter = 0
		n +=1
		#print(word)
		templist = [] #NP以降の文字列を切り出して一時保存するためのリスト
		if word.strip() == "NP":
			RBcounter = 1
			templist = parse[n:]
			#print(templist) #ここはちゃんと取れている

			# NPlistから最小単位のNPを抽出:かっこの数で括りを把握する
			NPwordlist = []
			for NPword_1 in templist:
				#print(NPword)
				if NPword_1 == "(":
					RBcounter += 1
				if NPword_1 == ")":
					RBcounter -= 1
				NPwordlist.append(NPword_1)
				if RBcounter == 0:
					#print(NPwordlist)
					break

			#やっと出力
			LRBflag = 0
			#print(NPwordlist)
			text = ""
			for NPword_2 in NPwordlist:
				if NPword_2 == ")":
					continue
				if NPword_2 == "(":
					LRBflag =1
					continue
				if NPword_2 != "(" and LRBflag ==1:
					LRBflag -=1
				else:
					if NPword_2 == "-LRB-":
						text += "("
					elif NPword_2 == "-RRB-":
						text += ")"
					else:
						text += NPword_2 + " "
			#print("*********************")
			#text += '\n'
			#print(text)
			output += text + '\n'

with codecs.open(out_file,'w','utf-8') as f:
	f.write(output)
