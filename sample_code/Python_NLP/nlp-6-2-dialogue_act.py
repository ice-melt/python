#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-6-2-dialogue_act.py
@Time       : 2019/5/7 11:43
@Version    : 1.0  
@Desc       : None
"""
import nltk

# 提取基本的消息数据
posts = nltk.corpus.nps_chat.xml_posts()[:10000]


# 定义一个简单的特征提取器,用于检测帖子包含什么词
def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains(%s)' % word.lower()] = True
    return features


# 构造训练和测试数据
# post.get('class') 获取帖子的对话行为类型
featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
"""
featuresets数据结构及部分结果
[
({'contains(now)': True, 'contains(im)': True, 'contains(left)': True, 'contains(with)': True, 'contains(this)': True, 'contains(gay)': True, 'contains(name)': True}, 'Statement'), 
({'contains(:)': True, 'contains(p)': True}, 'Emotion'), ...
]
"""

# 分割数据并进行训练 测试
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))  # 0.66
