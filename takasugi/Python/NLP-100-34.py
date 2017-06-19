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
pprint(file)
f = codecs.open(file[1], 'r', 'utf-8')
prev_2 = None
prev_1 = None
for l in f:
    # pprint(l)
    m = re.search('^EOS', l)
    if not m:
        w = MeCabNode(l)
        #pprint(w.to_map())
        if (prev_2 is not None) and (prev_1 is not None) and w.is_noun() and prev_1.surface == u'の' and prev_2.is_noun():
            print("{}{}{}").format(prev_2.surface.encode('utf-8'),prev_1.surface.encode('utf-8'),w.surface.encode('utf-8'))

        prev_2 = prev_1
        prev_1 = w
            
