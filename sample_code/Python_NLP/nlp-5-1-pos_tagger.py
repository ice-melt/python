#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt
@File       : nlp-5-1-pos_tagger.py
@Time       : 2019/4/18 19:01
@Version    : 1.0  
@Desc       :
	词性标注器
"""
import nltk

text = nltk.word_tokenize("And now for something completely different")
pos_tagger_result = nltk.pos_tag(text)
print(pos_tagger_result)

# 查看标记的文档
nltk.help.upenn_tagset('RB')
nltk.help.upenn_tagset('NN.*')
# nltk.[name].readme()  # the name is corpus name
print("============================= 同形同音异义词 ===============================")
# 同形同音异义词
text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
pos_tagger_result = nltk.pos_tag(text)
print(pos_tagger_result)
# refUSE->VBP REFuse->NN

print("============================== text.similar() =============================")
# text.similar() 找到所有词性想同的词
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
text.similar('woman')  # 名词
text.similar('bought')  # 动词
text.similar('over')  # 介词
text.similar('the')  # 限定词
# 该方法为词 w 找出所有上下文 w1ww2,再找出所有想同上下文中的词 w',即w1w'w2
