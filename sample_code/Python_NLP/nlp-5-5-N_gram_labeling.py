#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-5-5-N_gram_labeling.py
@Time       : 2019/4/22 14:36
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

# 一元标注器 ==================================================
# 通过在初始化标注器时指定已标注的句子数据作为参数来训练一元标注器
# 训练过程会检查每个词的标记,将所有词的最可能标记存储在一个字典里面
# 这个字典存储在标注器的内部
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
unigram_tagger_tag = unigram_tagger.tag(brown_sents[2007])
print(unigram_tagger_tag)
print(unigram_tagger.evaluate(brown_tagged_sents))

# 分离训练与测试数据 ===========================================
size = int(len(brown_tagged_sents) * 0.9)
print(size)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
unigram_tagger = nltk.UnigramTagger(train_sents)
print(unigram_tagger.evaluate(test_sents))

# 一般的 N-gram 的标注 ========================================
# NgramTagger 类,使用一个已标注的训练语料库来确定每个上下文中哪个词性标记最有可能
bigram_tagger = nltk.BigramTagger(train_sents)
bigram_tagger_tag = bigram_tagger.tag(brown_sents[2007])
print(bigram_tagger_tag)
unseen_sent = brown_sents[4203]
bigram_tagger_tag = bigram_tagger.tag(unseen_sent)
print(bigram_tagger_tag)
# 无法标注训练集中未看见过的词,也无法标注看见过但前面是None的词,所以准确度得分很低
print(bigram_tagger.evaluate(test_sents))
