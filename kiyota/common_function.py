# -*- coding: utf-8 -*-

#文書全体の形態素解析の結果のリスト [[文章1の形態素解析],[文章2の・・・],・・・]を返す
#文章ごとの形態素解析の結果はdictで保持{"surface":～～～,"base":～～～,"pos":～～～,"pos1":～～～}
def do_mecab(textfile):
    list_morpheme = [] #文章全体の解析結果
    import codecs
    import copy
    list_sentence = [] #文章単位の解析結果

    with codecs.open(textfile, 'r', 'utf-8') as f:
        for line in f:
            morpheme = line.split("\t") # 表層形とその他に分離
            if morpheme[0] != "　" and len(morpheme) != 1: # 空白とEOSは除外
                element = morpheme[1].split(",")
                dic = {"surface":morpheme[0],"base":element[6],"pos":element[0],"pos1":element[1]}
                list_sentence.append(dic)
            else:
                if len(list_sentence) != 0:
                    list_morpheme.append(copy.deepcopy(list_sentence))
                    list_sentence.clear()
    return list_morpheme
