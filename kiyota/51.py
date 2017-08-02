# -*- coding: utf-8 -*-
import re
import codecs

in_file = "output-50.txt"
out_file = "output-51.txt"
text = ""

p = re.compile(r"(?P<end>[\.:;!\?]) (?P<start>[A-Z])")

if __name__ == "__main__":
    with codecs.open(in_file,'r','utf-8') as f:
        for line in f:
            l = line.strip()
            l2 = re.sub(p,r"\g<end>\n\g<start>",l)
            for word in l2.split():
                match = re.search(r"[\.:;!\?]",word)
                if match:
                    # print(word + "\n")
                    text = text + word + "\n\n"
                else:
                    # print(word)
                    text = text + word + "\n"

    with codecs.open(out_file,'w','utf-8') as f1:
        f1.write(text)
