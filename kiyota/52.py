# -*- coding: utf-8 -*-
import re
import codecs
from nltk.stem.porter import PorterStemmer #work only with python2.7

in_file = "output-51.txt"
out_file = "output-52.txt"
output = ""

p = re.compile(r"[\.|\,|\n]")

if __name__ == "__main__":
    with codecs.open(in_file,'r','utf-8') as f:
        for line in f:
            stemmer = PorterStemmer()
            l = line.strip()
            if len(l) > 0:
				#print (l,stemmer.stem(l)) # 単語,語幹
                output = output + l + "\t" + stemmer.stem(l) + "\n"
            else:
                #print ""
                output = output + "\n"

    with codecs.open(out_file,'w','utf-8') as f1:
        f1.write(output)
