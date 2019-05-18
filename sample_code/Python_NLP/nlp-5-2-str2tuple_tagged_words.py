#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt
@File       : demo-5-2-str2tuple.py
@Time       : 2019/4/19 9:06
@Version    : 1.0  
@Desc       :

"""
import nltk

# ====================  str2tuple()   =======================
print('** 已标注标志符的标准字符串创建一个特殊元组 **')
tagged_token = nltk.tag.str2tuple('fly/NN')
print(tagged_token)

# ==================== tagged_words() =======================
print('** 语料库包含已标注的文本,可通过 tagged_words 访问 **')
print(nltk.corpus.nps_chat.tagged_words())
print(nltk.corpus.conll2000.tagged_words())

print('\n** 并非所有的语料库都采用同一组标记 **')
# tagged_words(simplify_tags=True)不能使用了
print(nltk.corpus.brown.tagged_words())
print(nltk.corpus.brown.tagged_words(tagset='universal'))
print(nltk.corpus.treebank.tagged_words())
print(nltk.corpus.treebank.tagged_words(tagset='universal'))

print("\n** 其他语言的已标注语料库 **")
print(nltk.corpus.sinica_treebank.tagged_words())  # 中文
print(nltk.corpus.indian.tagged_words())  # 印地语
print(nltk.corpus.mac_morpho.tagged_words())  # 葡萄牙语
print(nltk.corpus.conll2002.tagged_words())  #
print(nltk.corpus.cess_cat.tagged_words())  #

# ==================== tagged_sents() =======================
# 文中提到了此方法,但是目前没有例子
# 此方法将以标注的词划分成句子 P(199)




