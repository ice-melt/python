#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-7-1-ie_preprocess.py
@Time       : 2019/5/8 15:14
@Version    : 1.0  
@Desc       : None
"""
import nltk


def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)  # 句子分割器
    sentences = [nltk.word_tokenize(sent) for sent in sentences]  # 分词器
    sentences = [nltk.pos_tag(sent) for sent in sentences]  # 词性标注器
