#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-5-5-ambiguous_contexts.py
@Time       : 2019/4/22 16:31
@Version    : 1.0  
@Desc       : None
"""
import nltk
from nltk.corpus import brown

# 加载数据
brown_tagged_sents = brown.tagged_sents(categories='news')
# brown_tagged_words = brown.tagged_words(categories="news")
brown_sents = brown.sents(categories="news")
# brown_words = brown.words(categories="news")

# 性能限制 =========================================================
cfd = nltk.ConditionalFreqDist(
    ((x[1], y[1], z[0]), z[1])
    for sent in brown_tagged_sents
    for x, y, z in nltk.trigrams(sent)
)

ambiguous_context = [c for c in cfd.conditions() if len(cfd[c]) > 1]
print(sum(cfd[c].N() for c in ambiguous_context) / cfd.N())

# 混淆矩阵查看标注错误 ==============================================
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
test_tags = [tag for sent in brown.sents(categories='editorial') for (word, tag) in t2.tag(sent)]
gold_tags = [tag for (word, tag) in brown.tagged_words(categories='editorial')]
# print(nltk.ConfusionMatrix(gold_tags, test_tags))

# 句子层面的 N-gram 标注
print(t2.evaluate(test_sents))
