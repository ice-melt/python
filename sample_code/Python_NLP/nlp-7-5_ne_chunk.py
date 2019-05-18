#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-7-5_ne_chunk.py
@Time       : 2019/5/9 16:54
@Version    : 1.0  
@Desc       : None
"""
import nltk

sent = nltk.corpus.treebank.tagged_sents()[22]
# 如果设置参数binary=True,那么命名实体只被标注为NE,否则,分类器会添加类型标签,如 PERSON, ORGANIZATION and GPE 等
print(nltk.ne_chunk(sent, binary=True))
# (S
#   The/DT
#   (NE U.S./NNP)
#   is/VBZ
#   one/CD
#   ....
#   according/VBG
#   to/TO
#   (NE Brooke/NNP)
#   ...)
print(nltk.ne_chunk(sent))  # PERSON, ORGANIZATION and GPE
# (S
#   The/DT
#   (GPE U.S./NNP)
#   is/VBZ
#   one/CD
#   ......
#   according/VBG
#   to/TO
#   (PERSON Brooke/NNP T./NNP Mossman/NNP)
#   ....)
