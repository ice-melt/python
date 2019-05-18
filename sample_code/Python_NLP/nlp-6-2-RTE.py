#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-6-2-RTE.py
@Time       : 2019/5/8 10:24
@Version    : 1.0  
@Desc       : 识别文字蕴含(Recognizing textual entailment, RTE)
"""
import nltk


# rte默认没有下载,先进行下载
# nltk.download('rte')

# '识别文字蕴含'的特征提取器
def rte_features(rtepair):
    # RTEFeatureExtractor 类建立了一个在文本和假设中都有的并已去除一些停用词后的词汇包
    extractor = nltk.RTEFeatureExtractor(rtepair)
    features = {}
    # 计算重叠性和差异性
    features['word_overlap'] = len(extractor.overlap('word'))
    features['word_hyp_extra'] = len(extractor.hyp_extra('word'))
    features['ne_overlap'] = len(extractor.overlap('ne'))
    features['ne_hyp_extra'] = len(extractor.hyp_extra('ne'))
    return features


# Challenge 3,Pair 34.
rtepair = nltk.corpus.rte.pairs(['rte3_dev.xml'])[33]
extractor = nltk.RTEFeatureExtractor(rtepair)
print(extractor.text_words)
print(extractor.hyp_words)
print(extractor.overlap('word'))
print(extractor.overlap('ne'))
print(extractor.hyp_extra('word'))
"""
{'operation', 'Soviet', 'meeting', 'Davudi', 'Russia', 'terrorism.', 'Parviz', 'former', 'SCO', 'at', 'association', 'Organisation', 'binds', 'republics', 'fight', 'four', 'Asia', 'together', 'representing', 'that', 'China', 'fledgling', 'central', 'Iran', 'Shanghai', 'was', 'Co'}
{'member', 'SCO.', 'China'}
set()
{'China'}
{'member'}
"""
