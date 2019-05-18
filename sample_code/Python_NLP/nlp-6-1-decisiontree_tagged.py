#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-6-1-decisiontree_tagged.py
@Time       : 2019/4/23 19:16
@Version    : 1.0  
@Desc       : 词性标注
"""
from nltk.corpus import brown
import nltk

# 第5章 正则表达式标注器(手工标注的)
# 这里训练一个分类器 来算出哪个后缀最有信息量
suffix_fdist = nltk.FreqDist()

# 找出最常见的后缀
for w in brown.words():
    w = w.lower()
    suffix_fdist[w[-1:]] += 1
    suffix_fdist[w[-2:]] += 1
    suffix_fdist[w[-3:]] += 1
common_suffixes = list(suffix_fdist.keys())[:100]
print(common_suffixes)


# 定义特征提取器函数,检查给定单词的后缀
def pos_features(word):
    features = {}
    for suffix in common_suffixes:
        features['endswith(%s)' % suffix] = word.lower().endswith(suffix)
    return features


# 定义特征提取器,用来训练新的"决策树"的分类器
tagged_words = brown.tagged_words(categories='news')
featuresets = [(pos_features(n), g) for n, g in tagged_words]
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.DecisionTreeClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
print(classifier.classify(pos_features('cats')))
print(classifier.pseudocode(depth=4))
