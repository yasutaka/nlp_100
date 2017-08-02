# -*- coding: utf-8 -*-
import re
import codecs

in_file = "nlp.txt"
out_file = "output-50.txt"
text = ""

p = re.compile(r"(?P<end>[\.:;!\?]) (?P<start>[A-Z])")

if __name__ == "__main__":
    with codecs.open(in_file,'r','utf-8') as f:
        for line in f:
            l = line.strip()
            text = text + re.sub(p,r"\g<end>\n\g<start>",l)

    with codecs.open(out_file,'w','utf-8') as f1:
        f1.write(text)
