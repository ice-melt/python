#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-5-3-defaultdict.py
@Time       : 2019/4/19 17:21
@Version    : 1.0  
@Desc       : None
"""
import nltk
from nltk.corpus import brown

print("\n** 使用 UNK 替换低频词汇 **")
alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
vocab = nltk.FreqDist(alice)
v1000 = list(vocab)[:1000]
mapping = nltk.defaultdict(lambda: 'UNK')
for v in v1000:
    mapping[v] = v
alice2 = [mapping[v] for v in alice]
print(alice2[:10])
print(len(set(alice2)))

print("\n** 递增的更新字典 **")
counts = nltk.defaultdict(int)
for (word, tag) in brown.tagged_words(categories='news'):
    counts[tag] += 1

print("counts['NN'] = ", counts['NN'])
print(list(counts)[:5])

print("\n** itemgetter() **")
from operator import itemgetter

print(sorted(counts.items(), key=itemgetter(1), reverse=True)[:5])

# itemgetter() 指定排序键,一般情况下
# itemgetter(n) 返回一个函数,
# 这个函数可以在一些其他对象上被调用以获得该序列的第n个元素
pair = ('NP', 8336)
print("pair[1] => ", pair[1])
print("itemgetter(1)(pair) => ", itemgetter(1)(pair))

print("\n** nltk.Index()形式创建字典 **")
words = nltk.corpus.words.words('en')
anagrams = nltk.Index((''.join(sorted(w)), w) for w in words)
print(anagrams['aeilnrt'])
"""
['entrail', 'latrine', 'ratline', 'reliant', 'retinal', 'trenail']
"""

print("\n** 复杂的键和值 **")
pos = nltk.defaultdict(lambda: nltk.defaultdict(int))
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
for ((w1, t1), (w2, t2)) in nltk.bigrams(brown_news_tagged):
    pos[(t1, w2)][t2] += 1
print(pos[('DET', 'right')])
"""
defaultdict(<class 'int'>, {'NOUN': 5, 'ADJ': 11})
"""


print("\n** 颠倒词典 **")
counts = nltk.defaultdict(int)
for word in nltk.corpus.gutenberg.words('milton-paradise.txt'):
    counts[word] += 1
revers = [key for (key, value) in counts.items() if value == 32]
print(revers)
"""
['mortal', 'Against', 'Him', 'There', 'brought', 'King', 'virtue', 'every', 'been', 'thine']
"""
# 经常要进行反向查找,可建立一个映射值到键的字典
# 1. 每个key都有唯一个value值
pos = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
pos2 = dict((value, key) for (key, value) in pos.items())
print('颠倒词典后通过value取值pos2["N"]:%s' % pos2['N'])
# 2. 有几个value相同
pos.update({'cats': 'N', 'scratch': 'V', 'peacefully': 'ADV', 'old': 'ADJ'})
pos2 = nltk.defaultdict(list)
for key, value in pos.items():
    pos2[value].append(key)
print('颠倒词典(append)后通过value取值pos2["ADV"]:%s' % pos2['ADV'])
# nltk 索引支持进行相同的操作
pos2 = nltk.Index((value, key) for key, value in pos.items())
print('nltk 索引支持进行相同的操作取值pos2["ADV"]:%s' % pos2['ADV'])
