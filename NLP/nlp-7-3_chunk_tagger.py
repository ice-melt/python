#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-7-3_chunk_tagger.py
@Time       : 2019/5/9 14:07
@Version    : 1.0  
@Desc       : None
"""
from nltk.corpus import conll2000
import nltk

# nltk.download()


def npchunk_features(sentence, i, history):
    return demo1(sentence, i, history)


def demo1(sentence, i, history):
    word, pos = sentence[i]
    return {"pos": pos}  # 只提供当前标识符的词性标记


def demo2(sentence, i, history):
    word, pos = sentence[i]
    if i == 0:
        prevword, prevpos = "<START>", "<START>"
    else:
        prevword, prevpos = sentence[i - 1]
    return {"pos": pos, "prevpos": prevpos}  # 模拟相邻标记之间的相互作用


def demo3(sentence, i, history):
    word, pos = sentence[i]
    if i == 0:
        prevword, prevpos = "<START>", "<START>"
    else:
        prevword, prevpos = sentence[i - 1]
    return {"pos": pos, "word": word, "prevpos": prevpos}  # 为当前词增加特征,假设当前词的内容对分块有用


def demo4(sentence, i, history):
    word, pos = sentence[i]
    if i == 0:
        prevword, prevpos = "<START>", "<START>"
    else:
        prevword, prevpos = sentence[i - 1]
    if i == len(sentence) - 1:
        nextword, nextpos = "<END>", "<END>"
    else:
        nextword, nextpos = sentence[i + 1]
    return {"pos": pos,
            "word": word,
            "prevpos": prevpos,
            "nextpos": nextpos,
            "prevpos+pos": "%s+%s" % (prevpos, pos),
            "pos+nextpos": "%s+%s" % (pos, nextpos),
            "tags-since-dt": tags_since_dt(sentence, i)}  # 预取特征、配对功能和复杂的语境特征


def tags_since_dt(sentence, i):
    tags = set()
    for word, pos in sentence[:i]:
        if pos == "DT":
            tags = set()
        else:
            tags.add(pos)
    return '+'.join(sorted(tags))


# 基于分类器的NP分块器的基础代码
class ConsecutiveNPChunkTagger(nltk.TaggerI):
    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = npchunk_features(untagged_sent, i, history)
                train_set.append((featureset, tag))
                history.append(tag)
        self.classifier = nltk.MaxentClassifier.train(train_set, algorithm='megam', trace=0)  # 最大熵

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = npchunk_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)


class ConsecutiveNPChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        tagged_sents = [[((w, t), c) for (w, t, c) in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        self.tagger = ConsecutiveNPChunkTagger(tagged_sents)

    # 将标注器提供的标记序列转换回树
    def parse(self, sentence):
        tagged_sents = self.tagger.tag(sentence)
        conlltags = [(w, t, c) for ((w, t), c) in tagged_sents]
        return nltk.chunk.conlltags2tree(conlltags)

    def npchunk_features(sentence, i, history):
        word, pos = sentence[i]
        return {"pos": pos}  # 只提供当前标识符的词性标记


def main():
    # 使用CoNLL2000分块语料库训练
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
    train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])

    chunker = ConsecutiveNPChunker(train_sents)
    print(chunker.evaluate(test_sents))
    # ChunkParse
    # score:
    # IOB
    # Accuracy: 92.9 % %
    # Precision: 79.9 % %
    # Recall: 86.7 % %
    # F - Measure: 83.2 % %


if __name__ == '__main__':
    main()
