#
# -*- coding: utf-8 -*-


def cipher(x):
    out = ""

    for c in x:
        if (ord('a') - 1 < ord(c) and ord(c) < ord('z') + 1):
            out += chr(219 - ord(c))
        else:
            out += c

    return out

a = "a1b2c3D4"
print cipher(a)

