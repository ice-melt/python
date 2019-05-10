#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-7-3_baseline.py
@Time       : 2019/5/9 9:49
@Version    : 1.0  
@Desc       : None
"""
from nltk.corpus import conll2000
import nltk


def evaluate(chunk_types=['NP', 'VP', 'PP'], grammar=""):
    cp = nltk.RegexpParser(grammar)  # 不分块
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=chunk_types)
    print(cp.evaluate(test_sents))  # 评估结果


def demo1():
    evaluate(chunk_types=['NP'])


def demo2():
    evaluate(chunk_types=['NP'], grammar=r"NP: {<[CDJNP].*>+}")


def main():
    demo2()


if __name__ == '__main__':
    main()
