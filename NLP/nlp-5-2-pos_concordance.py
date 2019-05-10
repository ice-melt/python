#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt
@File       : nlp-5-2-pos_concordance.py
@Time       : 2019/4/19 15:03
@Version    : 1.0
@Desc       : None
"""
import nltk
from nltk.corpus import brown

# 研究一个词(比如 often ),看看它是如何使用,可以试着观察often后面的词
brown_learned_text = brown.words(categories='learned')
print(sorted(set(b for (a, b) in nltk.bigrams(brown_learned_text) if a == 'often')))

# 查看跟随词的词性标记
brown_lran_tagged = brown.tagged_words(categories='learned', tagset='universal')
tags = [b[1] for (a, b) in nltk.bigrams(brown_lran_tagged) if a[0] == 'often']
fd = nltk.FreqDist(tags)
fd.tabulate()
"""
often 后面最高频率的词性是动词,没有名词(该语料库中)
VERB  ADV  ADP  ADJ    .  PRT 
  37    8    7    6    4    2 
"""


# 使用 POS 标记寻找三词短语
def process(sentence):
    for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(sentence):
        if t1.startswith('V') and t2 == 'TO' and t3.startswith('V'):
            print(w1, w2, w3)


for tagged_sent in brown.tagged_sents():
    process(tagged_sent)

# 查看与它们的标记关系高度模糊不清的词
# 这些词各自的上下文可以帮助弄清楚标记之间的关系
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_news_tagged)
for word in data.conditions():
    if len(data[word]) > 3:
        tags = data[word].keys()
        print(word, ' '.join(tags))

# 打开 POS 一致性工具
nltk.app.concordance()

