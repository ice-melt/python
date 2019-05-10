#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-5-5-store_gram_tagger.py
@Time       : 2019/4/22 15:51
@Version    : 1.0
@Desc       : None
"""
import pickle
import nltk
from nltk.corpus import brown


# 序列化
def dump(filename, data):
    with open('%s.pkl' % filename, 'wb') as f:
        pickle.dump(data, f)


# 反序列化
def load(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


# 加载数据
brown_tagged_sents = brown.tagged_sents(categories='news')
# brown_tagged_words = brown.tagged_words(categories="news")
# brown_sents = brown.sents(categories="news")
# brown_words = brown.words(categories="news")
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

# 组合标注器
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
print(t2.evaluate(test_sents))

# 将标注器 t2 保存到文件 t2.pkl
dump('t2', t2)

# 载入保存的标注器,并进行标注
tagger = load('t2.pkl')
text = """The board's action shows what free enterprise
is up against in our complex maze of regulatory laws ."""
tokens = text.split()
print(tagger.tag(tokens))
