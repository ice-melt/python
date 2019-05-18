#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-7-4_loop_parse.py
@Time       : 2019/5/9 15:12
@Version    : 1.0  
@Desc       : None
"""
import nltk

grammar = r"""
   NP: {<DT|JJ|NN.*>+}
   PP: {<IN><NP>}
   VP: {<VB.*><NP|PP|CLAUSE>+$}
   CLAUSE: {<NP><VP>}
"""
cp = nltk.RegexpParser(grammar)
sentence = [("Mary", "NN"), ("saw", "VBD"), ("the", "DT"), ("cat", "NN"), ("sit", "VB"), ("on", "IN"), ("the", "DT"),
            ("mat", "NN")]
print(cp.parse(sentence))
"""
(S
  (NP Mary/NN)
  saw/VBD
  (CLAUSE
    (NP the/DT cat/NN)
    (VP sit/VB (PP on/IN (NP the/DT mat/NN)))))
"""

sentence = [("John", "NNP"), ("thinks", "VBZ"), ("Mary", "NN"),
            ("saw", "VBD"), ("the", "DT"), ("cat", "NN"), ("sit", "VB"),
            ("on", "IN"), ("the", "DT"), ("mat", "NN")]
print(cp.parse(sentence))
"""
(S
  (NP John/NNP)
  thinks/VBZ
  (NP Mary/NN)
  saw/VBD
  (CLAUSE
    (NP the/DT cat/NN)
    (VP sit/VB (PP on/IN (NP the/DT mat/NN)))))
"""
cp = nltk.RegexpParser(grammar, loop=2)  # 添加循环
print(cp.parse(sentence))
"""
(S
  (NP John/NNP)
  thinks/VBZ
  (CLAUSE
    (NP Mary/NN)
    (VP
      saw/VBD
      (CLAUSE
        (NP the/DT cat/NN)
        (VP sit/VB (PP on/IN (NP the/DT mat/NN)))))))
"""
