
import chardet
from itertools import cycle

class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def print_all(self):
        return self.surface + "\t" + self.base + ", " + self.pos + ", " + self.pos1

def read_morpheme(cabochafile):
    sentences = []
    sentence = []
    for line in cabochafile:
        if line == "EOS\n":
            sentences.append(sentence)
            sentence = []
        elif line[0] == "*":
            continue
        else:
            surface, other = line.split()
            others = other.split(",")
            base, pos, pos1 = others[6], others[0], others[1]
            morph = Morph(surface, base, pos, pos1)
            sentence.append(morph)
    return sentences

if __name__ == "__main__":
    f = open("neko.txt.cabocha", "r")
    sentences = read_morpheme(f)
    for morph in sentences[2]:
        print morph.print_all()
    f.close()


# cas