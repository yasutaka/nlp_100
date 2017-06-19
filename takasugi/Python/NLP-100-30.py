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

for l in f:
    # pprint(l)
    m = re.search('^EOS', l)
    if not m:
        w = MeCabNode(l)
        #pprint(w.to_map())
        if w.is_verb():
            print("{}:{}").format(w.surface.encode('utf-8'), w.base.encode('utf-8'))
