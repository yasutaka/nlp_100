# -*- coding: utf-8 -*-

#author: Alex

######
####### Deprecated: 57 and 58 still in progress. The requested 'collapsed-dependency' is not supported anymore by StanfordNLPcore ########
####### BUG: StanfordNLPcore cannot process big documents. It will crash by the end of nlp.txt. the code will run 80% of txt #######
#######

import re
import json
import corenlp #need JAVA jdk install to run
#from pycorenlp import StanfordCoreNLP
import itertools
import pprint
p = pprint.pprint
from pycorenlp import StanfordCoreNLP
from collections import defaultdict
import pydot

#53 ~
nlp = StanfordCoreNLP('http://localhost:9000')


clean_doc_file = []
with open('nlp.txt', 'r') as f:
    for l in f:
        l = l.strip('\n')
        l = re.sub(re.escape('.'),'\n', l)
        l = re.sub(re.escape(';'),'\n', l)
        l = re.sub(re.escape('?'),'\n', l)
        l = re.sub(re.escape('!'),'\n', l)
        l = re.sub(re.escape(':'),'\n', l)
        l = re.sub(re.escape(','),'\n', l)
        clean_doc_file.append(l)

####clean_doc_file = ['he is alex. He likes the sea.','dog'] ### for testing
with open('nlp_54.txt', 'a+') as w:
    with open('nlp_55.txt', 'a+') as w2:
        with open('nlp_s_shiki.txt', 'a+') as w3:
            
            for t in clean_doc_file:
                output = nlp.annotate(t, properties={
                'annotators': 'tokenize,pos,lemma,ner,dcoref',
                'outputFormat': 'json'
                })
                #p(output)
                if (output['sentences']):
                    x = output['sentences']
                    for xx in x:
                        f = xx['tokens']
                        for ff in f:
                            #54
                            w.write(ff['word'] +'\t'+ ff['lemma'] +'\t'+ ff['pos'] + '\n')
                            #55
                            if (ff['ner'] == 'PERSON'):
                                w2.write(ff['word'] + '\n')     
                    
                    #56
                    y = output['corefs']
                    x = re.findall(re.escape("'isRepresentativeMention': True"), str(y))
                    if x:
                        y = re.findall('text?.+?,', str(y))
                        #print y
                    
                    #59 
                    x = output['sentences']
                    for xx in x:
                        f = xx['parse']
                        w3.write(f)
                        

                    # #57 + 58 _start
                    
                    #Collapsed dependency not supported anymore. Dont know how to solve this.