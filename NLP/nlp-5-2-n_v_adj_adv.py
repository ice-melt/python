#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt
@File       : nlp-5-2-n_v_adj_adv.py
@Time       : 2019/4/19 11:28
@Version    : 1.0  
@Desc       : None
"""
import nltk

# 图形化 POS 一致性工具
# nltk.app.concordance()  # 寻找任一词和 POS 标记的组合

# ==================== 简化的词性标记集 =======================
print("\n")
brown_news_tagged = nltk.corpus.brown.tagged_words(categories='news', tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
print(tag_fd.items())
# tag_fd.plot(cumulative=True)  # 显示频率分布绘图

# ==================== 名词 =======================
print("\n** 名词 **")
word_tag_pairs = nltk.bigrams(brown_news_tagged)  # 构建双连词词汇表
"""
word_tag_pairs 结构如下:
[	(
		('The', 'DET'), ('Fulton', 'NOUN')
	), 
	(
		('Fulton', 'NOUN'), ('County', 'NOUN')
	),
	...
]
"""
print(list(nltk.FreqDist(a[1] for (a, b) in word_tag_pairs if b[1].startswith('N'))))

# ==================== 动词 =======================
print("\n** 动词 **")
wsj = nltk.corpus.treebank.tagged_words()  # 新闻文本
# 按频率排序所有动词
word_tag_fd = nltk.FreqDist(wsj)
print([word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('V')])
# 词作为条件,标记作为事件,即给定单词时可能出现的标记
cfd1 = nltk.ConditionalFreqDist(wsj)
print(cfd1['yield'].keys())
# 以标记作为条件,词作为事件,即查看对于给定标记的可能词
cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in wsj)
print(cfd2['VB'].keys())
# VD(过去式) VN(过去分词) 区别:
# 找到同是 VD 和 VN 的词汇
print([w for w in cfd1.conditions() if 'VBD' in cfd1[w] and 'VBN' in cfd1[w]])
# 看看这个词周围的文字的情况
idx1 = wsj.index(('kicked', 'VBD'))
print(wsj[idx1 - 4:idx1 + 1])
idx2 = wsj.index(('kicked', 'VBN'))
print(wsj[idx2 - 4:idx2 + 1])

# ==================== 形容词和副词 =======================
print("\n** 形容词和副词 **")
