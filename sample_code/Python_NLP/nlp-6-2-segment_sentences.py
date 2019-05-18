#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-6-q`a     -sentence_split.py
@Time       : 2019/5/7 11:15
@Version    : 1.0  
@Desc       : None
"""
import nltk


def punct_features(tokens, i):
    return {'next-word-capitalized': tokens[i + 1][0].isupper(),
            'prevword': tokens[i - 1].lower(),
            'punct': tokens[i],
            'prev-word-is-one-char': len(tokens[i - 1]) == 1}


def segment_sentences(words, classifier):
    start = 0
    sents = []
    for i, word in words:
        if word in '.?!' and classifier.classify(punct_features(words, i)):
            sents.append(words[start:i + 1])
            start = i + 1
    if start < len(words):
        sents.append(words[start:])
        return sents


def main():
    sents = nltk.corpus.treebank_raw.sents()

    # 单独句子标识符的合并链表
    tokens = []

    # 包含所有句子-边界标识符索引的集合
    boundaries = set()
    offset = 0
    for sent in sents:
        tokens.extend(sent)
        offset += len(sent)
        boundaries.add(offset - 1)

    print(tokens)
    featuresets = [(punct_features(tokens, i), (i in boundaries))
                   for i in range(1, len(tokens) - 1)
                   if tokens[i] in '.?!']

    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print(nltk.classify.accuracy(classifier, test_set))


if __name__ == '__main__':
    main()
