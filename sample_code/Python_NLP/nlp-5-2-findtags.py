#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt
@File       : nlp-5-2-findtags.py
@Time       : 2019/4/19 14:23
@Version    : 1.0  
@Desc       : 找出最频繁的名词标记的程序
"""
import nltk


def findtags(tag_prefix, tagged_text):
	cfd = nltk.ConditionalFreqDist(
		(_tag, word) for (word, _tag) in tagged_text if _tag.startswith(tag_prefix)
	)
	# keys() 不让切片,转成list
	return dict((_tag, list(cfd[_tag].keys())[:5]) for _tag in cfd.conditions())


print("** 找出最频繁的名词标记的程序 **")
tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))
for tag in sorted(tagdict):
	print(tag, tagdict[tag])
