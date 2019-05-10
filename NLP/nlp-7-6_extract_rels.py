#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-7-6_extract_rels.py
@Time       : 2019/5/9 17:09
@Version    : 1.0  
@Desc       : None
"""
import re
import nltk

IN = re.compile(r'.*\bin\b(?!\b.+ing)')  # 否定预测先行断言
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern=IN):
        print(nltk.sem.relextract.rtuple(rel))

# [ORG: 'WHYY'] 'in' [LOC: 'Philadelphia']
# [ORG: 'McGlashan &AMP; Sarrail'] 'firm in' [LOC: 'San Mateo']
# [ORG: 'Freedom Forum'] 'in' [LOC: 'Arlington']
# [ORG: 'Brookings Institution'] ', the research group in' [LOC: 'Washington']
# [ORG: 'Idealab'] ', a self-described business incubator based in' [LOC: 'Los Angeles']
# [ORG: 'Open Text'] ', based in' [LOC: 'Waterloo']
# [ORG: 'WGBH'] 'in' [LOC: 'Boston']
# [ORG: 'Bastille Opera'] 'in' [LOC: 'Paris']
# [ORG: 'Omnicom'] 'in' [LOC: 'New York']
# [ORG: 'DDB Needham'] 'in' [LOC: 'New York']
# [ORG: 'Kaplan Thaler Group'] 'in' [LOC: 'New York']
# [ORG: 'BBDO South'] 'in' [LOC: 'Atlanta']
# [ORG: 'Georgia-Pacific'] 'in' [LOC: 'Atlanta']
from nltk.corpus import conll2002

vnv = """
(
is/V| # 3rd sing present and
was/V| # past forms of the verb zijn ('be')
werd/V| # and also present
wordt/V # past of worden ('become')
)
.* # followed by anything
van/Prep # followed by van ('of')
"""

VAN = re.compile(vnv, re.VERBOSE)
for doc in conll2002.chunked_sents('ned.train'):
    for r in nltk.sem.extract_rels('PER', 'ORG', doc, corpus='conll2002', pattern=VAN):
        print(nltk.sem.relextract.clause(r, relsym="VAN"))
# VAN("cornet_d'elzius", 'buitenlandse_handel')
# VAN('johan_rottiers', 'kardinaal_van_roey_instituut')
# VAN('annie_lennox', 'eurythmics')

for doc in conll2002.chunked_sents('ned.train'):
    for r in nltk.sem.extract_rels('PER', 'ORG', doc, corpus='conll2002', pattern=VAN):
        print(nltk.sem.relextract.rtuple(r, lcon=True, rcon=True))
# ...'')[PER: "Cornet/V d'Elzius/N"] 'is/V op/Prep dit/Pron ogenblik/N kabinetsadviseur/N van/Prep staatssecretaris/N voor/Prep' [ORG: 'Buitenlandse/N Handel/N'](''...
# ...'')[PER: 'Johan/N Rottiers/N'] 'is/V informaticacoördinator/N van/Prep het/Art' [ORG: 'Kardinaal/N Van/N Roey/N Instituut/N']('in/Prep'...
# ...'Door/Prep rugproblemen/N van/Prep zangeres/N')[PER: 'Annie/N Lennox/N'] 'wordt/V het/Art concert/N van/Prep' [ORG: 'Eurythmics/N']('vandaag/Adv in/Prep'...
