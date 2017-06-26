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

out = {}

for l in f:
    # pprint(l)
    m = re.search('^EOS', l)
    if not m:
        w = MeCabNode(l)
        #pprint(w.to_map())
        if w.base in out.keys():
            out[w.base] += 1
        else:
            out[w.base] = 1

o_out = sorted(out.items(), key=lambda x: x[1], reverse=True)

ind = 0
tops = []
for oout in o_out:
    print("{}:{}").format(oout[0].encode('utf-8'), oout[1])
    if ind < 10:
        tops.append(oout)
        ind += 1



#
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
y_data = []
x_data = []
for d in tops:
    y_data.append(d[0])
    x_data.append(d[1])

y_pos = np.arange(len(y_data))

ax.barh(y_pos, x_data, color='red')

ax.set_yticks(y_pos)
ax.set_yticklabels(y_data)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Frequency')
ax.set_title('Word-Frequency')

plt.show()

