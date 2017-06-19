# -*- coding: utf-8 -*-
import re
from pprint import pprint

class MeCabNode:
    def __init__(self, base_str):
        self.set_data(base_str)

    def set_data(self, str):
        tmp = re.split(u'\t', str)
        self.surface = tmp[0]
        ary = tmp[1].split(',')
        #pprint(ary)
        self.pos = ary[0]
        self.pos1 = ary[1]
        self.base = ary[6]

    def to_map(self):
        return dict(surface=self.surface, pos=self.pos, pos1=self.pos1,
                    base=self.base)

    def is_noun(self):
        if self.pos == u'名詞':
            return True
        else:
            return False

    def is_verb(self):
        if self.pos == u'動詞':
            return True
        else:
            return False

    def is_sahen(self):
        if self.pos == u'名詞' and self.pos1 == u'サ変接続':
            return True
        else:
            return False


if __name__ == "__main__":
    str = "surface pos,pos1,2,3,4,5,base"
    mn = MeCabNode(str)
    out = mn.to_map()
    pprint(out)
