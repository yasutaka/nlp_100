# -*- coding:utf-8 -*-
def generate_text(**kwargs):
    return str(kwargs['x']) + "時の" + kwargs['y'] + "は" + str(kwargs['z'])

print generate_text(x=12, y="気温", z=22.4)
