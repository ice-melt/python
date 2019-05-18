#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt
@File       : nlp_util.py
@Time       : 2019/4/11 11:22
@Version    : 1.0  
@Desc       : None
"""
import nltk


def plural(word):
	"""
	简单的单数转复数函数,部分字词会转换失败,例如 fan
	:param word:
	:return:
	"""
	if word.endswith('y'):
		return word[:-1] + 'ies'
	elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
		return word + "es"
	elif word.endswith("an"):
		return word[:-2] + 'en'
	else:
		return word + "s"


def unusual_words(text):
	"""
	寻找文本语料中不常见的活拼写错误的词汇
	:param text:
	:return:
	"""
	text_vocab = set(w.lower() for w in text if w.isalpha())
	# 词汇语料库是 UNIX 中的/usr/dict/words文件
	english_vocab = set(w.lower() for w in nltk.corpus.words.words())
	unusual = text_vocab.difference(english_vocab)
	return sorted(unusual)


def content_fraction(text):
	"""
	计算文本中不包含在停用词列表中的词所占的比例
	:param text:
	:return:
	"""
	# 停用语料库(一些高频词汇)
	stopwords = nltk.corpus.stopwords.words("english")
	content = [w for w in text if w.lower() not in stopwords]
	return len(content) / len(text)


def get_target(puzzle_letter, obligatory):
	puzzle_letters = nltk.FreqDist(puzzle_letter)
	word_list = nltk.corpus.words.words()
	res = [
		w for w in word_list if len(w) >= 6
								and obligatory in w
								and nltk.FreqDist(w) <= puzzle_letters
	]
	print(res)


def name_corpus():
	names = nltk.corpus.names
	fileids = names.fileids()
	print("names.fileids()=%s" % fileids)
	male_names = names.words(fileids[1])
	female_names = names.words(fileids[0])
	common = [w for w in male_names if w in female_names]
	print("男女都使用的名字:%s" % common)
	cfd = nltk.ConditionalFreqDist(
		(fileid, name[-1])
		for fileid in fileids
		for name in names.words(fileid)
	)
	import matplotlib
	cfd.plot()


def cmudict_corpus():
	entries = nltk.corpus.cmudict.entries()
	print("the entries size is %d" % len(entries))
	for entry in entries[39943:39951]:
		print(entry)
	# 找到押韵的词
	syllable = ['N', 'IHO', 'K', 'S']
	import operator
	ssw = [word for word, pron in entries if operator.eq(pron[-4:], syllable)]
	print(ssw)
	print([w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n'])
	print(sorted(set(w[:2] for w, pron in entries if pron[0] == 'N' and w[0] != 'n')))

	print([w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']])


def stress(pron):
	return [char for phone in pron for char in phone if char.isdigit()]


if __name__ == '__main__':
	print(plural("wish"))
	print(plural("fan"))
	# === 不常用的词或拼写错误的词
	# r1 = unusual_words(nltk.corpus.gutenberg.words("austen-sense.txt"))
	# print(r1)
	# r2 = unusual_words(nltk.corpus.nps_chat.words())
	# print(r2)
	# === 筛除高频词
	# r3 = content_fraction(nltk.corpus.reuters.words())
	# print(r3)
	# get_target("egivrvonl", "r")
	# name_corpus()
	cmudict_corpus()
