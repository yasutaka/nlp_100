# -*- coding: utf-8 -*-
#
import sys
import re
import codecs
from pprint import pprint

from nlp100common import MeCabNode

argvs = sys.argv

#
#
file = sys.argv
#pprint(file)
f = codecs.open(file[1], 'r', 'utf-8')
out = list()
out.append(list())

prev = None
for l in f:
    # pprint(l)
    m = re.search('^EOS', l)
    if not m:
        w = MeCabNode(l)
        if w.is_noun():
            out[-1].append(w)
        elif prev is None or prev.is_noun():
            out.append(list())
            
        prev = w


out2 = sorted(out, key=lambda x: len(x))

for o in out2:
    o_str = ''
    for oo in o:
        o_str += ":" + oo.surface.encode('utf-8')
    print("{}: {}").format(len(o), o_str)


            
