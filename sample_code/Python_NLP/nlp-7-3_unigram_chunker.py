#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-7-3_unigram_chunker.py
@Time       : 2019/5/9 10:24
@Version    : 1.0  
@Desc       : 使用unigram标注器对名词短语分块
"""
from nltk.corpus import conll2000
import nltk


# 使用训练语料找到对每个词性标记最有可能的块标记(I、O或B)
# 可以用unigram标注器建立一个分块器,但不是要确定每个词的正确词性标记,而是给定每个词的词性标记,尝试确定正确的块标记
class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t, c) for w, t, c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        # self.tagger = nltk.UnigramTagger(train_data)
        self.tagger = nltk.UnigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word, pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        # 为词性标注IOB块标记
        conlltags = [(word, pos, chunktag) for ((word, pos), chunktag) in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)  # 转换成分块树状图


class BigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t, c) for w, t, c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        # self.tagger = nltk.UnigramTagger(train_data)
        self.tagger = nltk.BigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word, pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        # 为词性标注IOB块标记
        conlltags = [(word, pos, chunktag) for ((word, pos), chunktag) in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)  # 转换成分块树状图


def main():
    # 使用CoNLL2000分块语料库训练
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
    train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
    # chunker = UnigramChunker(train_sents)
    chunker = BigramChunker(train_sents)

    print(chunker.evaluate(test_sents))
    # ChunkParse score:
    #     IOB Accuracy:  92.9%%
    #     Precision:     79.9%%
    #     Recall:        86.8%%
    #     F-Measure:     83.2%%
    postags = sorted(set(pos for sent in train_sents for (word, pos) in sent.leaves()))
    print(chunker.tagger.tag(postags))
    # [(u'#', u'B-NP'), (u'$', u'B-NP'), (u"''", u'O'), (u'(', u'O'), (u')', u'O'), (u',', u'O'), (u'.', u'O'), (u':', u'O'), (u'CC', u'O'), (u'CD', u'I-NP'), (u'DT', u'B-NP'), (u'EX', u'B-NP'), (u'FW', u'I-NP'), (u'IN', u'O'), (u'JJ', u'I-NP'), (u'JJR', u'B-NP'), (u'JJS', u'I-NP'), (u'MD', u'O'), (u'NN', u'I-NP'), (u'NNP', u'I-NP'), (u'NNPS', u'I-NP'), (u'NNS', u'I-NP'), (u'PDT', u'B-NP'), (u'POS', u'B-NP'), (u'PRP', u'B-NP'), (u'PRP$', u'B-NP'), (u'RB', u'O'), (u'RBR', u'O'), (u'RBS', u'B-NP'), (u'RP', u'O'), (u'SYM', u'O'), (u'TO', u'O'), (u'UH', u'O'), (u'VB', u'O'), (u'VBD', u'O'), (u'VBG', u'O'), (u'VBN', u'O'), (u'VBP', u'O'), (u'VBZ', u'O'), (u'WDT', u'B-NP'), (u'WP', u'B-NP'), (u'WP$', u'B-NP'), (u'WRB', u'O'), (u'``', u'O')]


if __name__ == '__main__':
    main()
