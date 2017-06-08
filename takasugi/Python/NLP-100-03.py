#
# -*- coding: utf-8 -*-
import re

check_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

print filter(lambda a: a != 0, map(lambda n: len(n), re.split(r"[,¥. ]", check_str)))




