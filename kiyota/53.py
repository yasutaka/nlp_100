# -*- coding: utf-8 -*-
# pyton2.7で実行
import os
import subprocess
import xml.etree.ElementTree as ET
import codecs

fname = 'nlp.txt'
fname_parsed = 'nlp.txt.xml'
out_file = "output-53.txt"

def parse_nlp():
    if not os.path.exists(fname_parsed):
        # StanfordCoreNLP実行
        subprocess.call(
			'java -cp "/Users/USER/Documents/nlp_100/python/Chapter6/stanford-corenlp-full-2013-06-20/*"'
			#'java -cp "/Users/USER/Documents/nlp_100/python/Chapter6/stanford-corenlp-full-2017-06-09/*"'
            ' -Xmx2g'
            ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
            ' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
            ' -file ' + fname,
            shell=True     # shellで実行
        )

# nlp.txtを解析 -> nlp.txt.xmlができる
parse_nlp()

# xmlファイルの読み込み
tree = ET.parse(fname_parsed)
root = tree.getroot()

# wordの値を取得
output = ""
for e in root.findall(".//word"):
	output = output + e.text + '\n'

with codecs.open(out_file,'w','utf-8') as f:
	f.write(output)
