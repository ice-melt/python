#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-5-4-automatic_labeling.py
@Time       : 2019/4/22 10:43
@Version    : 1.0  
@Desc       : None
"""
import nltk
from nltk.corpus import brown

# 加载数据
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_tagged_words = brown.tagged_words(categories="news")
brown_sents = brown.sents(categories="news")
brown_words = brown.words(categories="news")

print(brown_tagged_sents[0:5])
print(brown_sents[0:5])

# 默认标注器 ==========================================================
tags = [tag for (word, tag) in brown_tagged_words]
tag_max = nltk.FreqDist(tags).max()  # 最有可能的标记
print("最有可能的标记==>%s" % tag_max)

# 创建一个将所有词都标注成 NN 的标注器
raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
tokens = nltk.word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN')
default_tagger_words = default_tagger.tag(tokens)
print("所有词都标注成 NN:\n%s" % default_tagger_words)
# 标注效果,不好,只标注正确了八分之一的标识符
print("标注效果:%s" % default_tagger.evaluate(brown_tagged_sents))

# 正则表达式标注器 ====================================================
# 基于匹配模式分配标记给标识符,例如一般情况下认为
# 以ed结尾的词都是动词过去分词,
# 以's结尾的词都是名词所有格
patterns = [
    (r'.*ing$', 'VBG'),  # gerunds
    (r'.*ed$', 'VBD'),  # simple past
    (r'.*es$', 'VBZ'),  # 3rd singular present
    (r'.*ould$', 'MD'),  # modals
    (r'.*\'s$', 'NN$'),  # possessive nouns
    (r'.*s$', 'NNS'),  # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'.*', 'NN')  # nouns(default)
]

regexp_tagger = nltk.RegexpTagger(patterns)
regexp_tagger_words = regexp_tagger.tag(brown_sents[3])
print("正则标注成 :\n%s" % regexp_tagger_words)
print("标注效果:%s" % regexp_tagger.evaluate(brown_tagged_sents))

# 查找标注器 =========================================================
fd = nltk.FreqDist(brown_words)
cfd = nltk.ConditionalFreqDist(brown_tagged_words)
most_freq_words = list(fd.keys())[:100]
likely_tags = dict((word, cfd[word].max()) for word in most_freq_words)
baseline_tagger = nltk.UnigramTagger(model=likely_tags)
print("查找标注器结果 :\n%s" % baseline_tagger)
print("标注效果:%s" % baseline_tagger.evaluate(brown_tagged_sents))

sent = brown_sents[3]
print(baseline_tagger.tag(sent))

baseline_tagger = nltk.UnigramTagger(model=likely_tags, backoff=nltk.DefaultTagger('NN'))
print("查找标注器结果 :\n%s" % baseline_tagger)
print("标注效果:%s" % baseline_tagger.evaluate(brown_tagged_sents))
