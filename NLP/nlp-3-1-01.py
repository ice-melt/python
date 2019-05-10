#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt
@File       : nlp-3-1-01.py
@Time       : 2019/4/11 17:17
@Version    : 1.0  
@Desc       : None
"""
from urllib.request import urlopen
import nltk


def download():
	# url = "http://www.gutenberg.org/cache/epub/24185/pg24185-images.html"
	# url = "http://www.gutenberg.org/files/2554/2554.txt"
	url = "https://www.gutenberg.org/files/2554/2554-0.txt"
	return urlopen(url).read()


def write2file(content):
	with open("crime_and_punishment_2554.txt", 'wb') as file:
		file.write(content)


def read_data():
	content = []
	# utf-8-sig 编码可以去除 \ufeff
	with open("crime_and_punishment_2554.txt", encoding="utf-8-sig") as file:
		content.extend(line.replace("\n", "") for line in file.readlines() if line != '\n')
	return content


if __name__ == '__main__':
	# write2file(download())
	data = read_data()
	print(data[:3])
	raw = "".join(str(s) for s in read_data())
	print(type(raw))
	print(len(raw))
	print(raw[1404478:1404678])

	tokens = nltk.word_tokenize(raw)
	print(len(tokens))
	print(tokens[:10])
	text = nltk.Text(tokens)

	s = raw.find("PART I")
	e = raw.rfind("End of Project Gutenberg’s Crime")
	"""
	End of Project Gutenberg’s Crime
	End of Project Gutenberg’s Crime
	"""
	print(s, e)

	raw = raw[5071:1113619]
	print(raw.find("PART I"))
