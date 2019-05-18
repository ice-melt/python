#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-5-4-labeling_performance.py
@Time       : 2019/4/22 14:05
@Version    : 1.0  
@Desc       : None
"""
import nltk
from nltk.corpus import brown


def performance(cfd, wordlist, brown_tagged_sents):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown_tagged_sents)


def display():
    import pylab
    brown_tagged_sents = brown.tagged_sents(categories='news')
    brown_tagged_words = brown.tagged_words(categories="news")
    # brown_sents = brown.sents(categories="news")
    brown_words = brown.words(categories="news")

    words_by_freq = list(nltk.FreqDist(brown_words))
    cfd = nltk.ConditionalFreqDist(brown_tagged_words)
    sizes = 2 ** pylab.arange(15)
    perfs = [performance(cfd, words_by_freq[:size], brown_tagged_sents) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()


display()
