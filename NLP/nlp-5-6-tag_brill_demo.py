#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-5-6-tag_brill_demo.py
@Time       : 2019/4/22 17:42
@Version    : 1.0  
@Desc       : None
"""
import nltk

ll = [t for t in nltk.tag.brill.nltkdemo18()]
print(ll)