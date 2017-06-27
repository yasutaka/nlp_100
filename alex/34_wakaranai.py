from natto import MeCab
import chardet
from itertools import cycle

tex = ['私の猫です。','飲みに行くの？']
big = []
mini = []

with MeCab('-F%f[1]') as nm:
    for t in tex:
        for n in nm.parse(t, as_nodes=True):
            if not n.is_eos() and n.is_nor():
            #klass, word = n.feature.split(',', 1)
                y = n.feature
                tango = n.surface
                mini.append({"tango":tango,"y":y})
                # if (y == '連体化'):
                #     mini.append(tango)
    print mini
    for sentence in mini:
        for index in range(1,len(sentence) - 1):
            if sentence[index - 1]["pos"] == "名詞" and sentence[index]["surface"] == "の" and sentence[index + 1]["pos"] == "名詞":
                print(sentence[index - 1]["surface"] + sentence[index]["surface"] + sentence[index + 1]["surface"])





    # for t in tex:
    #     for n in nm.parse(t, as_nodes=True):
    #         #if not n.is_eos() and n.is_nor():
    #         #klass, word = n.feature.split(',', 1)
    #         y = n.feature
    #         tango = n.surface
    #         if (y == '連体化'):
    #             mini.append(tango)


# for tt in t:
#     l = (nm.parse(tt))
#     print l
#     for ll in l:
#         print ll
#         print chardet.detect(ll)


# with open("neko_hen.txt", "w+"): pass
# text = open("neko.txt","r+")
# res_file = open("neko_hen.txt", "a+")
# reader = text.readlines()
# for line in reader:
# with MeCab('-F%f[1],%f[6]') as nm:
#     n = nm.parse(line, as_nodes=True)
#     print n
#     #if not n.is_eos() and n.is_nor():
#     klass, word = n.feature.split(',', 1)
#     if klass in ['連体化']: #['名詞', '形容詞', '形容動詞','動詞']:
#         print word
                # res_file.write(word + ' ')
                # res_file.write('\n')