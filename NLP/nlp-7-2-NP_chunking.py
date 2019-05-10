#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-7-2-NP_chunking.py
@Time       : 2019/5/8 17:29
@Version    : 1.0  
@Desc       : 一个简单的基于正则表达式的NP分块器的例子
"""
import nltk


def demo1():
    # 已标注词性的例句
    sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),
                ("the", "DT"), ("cat", "NN")]
    # 正则表达式规则定义NP-分块语法:由可选的且后面跟着任意数目形容词(JJ)的限定词和名词(NN)组成
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(sentence)
    print(result)

    result.draw()


def demo2():
    sentence = [("another", "DT"), ("sharp", "JJ"), ("dive", "NN"),
                ("trade", "NN"), ("figures", "NNS"),
                ("any", "DT"), ("new", "JJ"), ("policy", "NN"), ("measures", "NNS"),
                ("earlier", "JJR"), ("stages", "NNS"),
                ("Panamanian", "JJ"), ("dictator", "NN"), ("Manuel", "NNP"), ("Noriega", "NNP")]
    # 正则表达式规则定义NP-分块语法:由可选的且后面跟着任意数目形容词(JJ)的限定词和名词(NN)组成
    grammar = "NP: {<DT>?<JJ.*>*<NN.*>+}"
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(sentence)
    print(result)

    result.draw()


def demo3():
    # his/PRP$ Mansion/NNP House/NNP speech/NN
    # the/DT price/NN cutting/VBG
    # 3/CD %/NN to/TO 4/CD %/NN
    # more/JJR than/IN 10/CD %/NN
    # the/DT fastest/JJS developing/VBG trends/NNS
    # 's/POS skill/NN
    nltk.app.chunkparser()


def demo_regexp_parser():
    grammar = r"""
       NP: {<DT|PP\$>?<JJ>*<NN>}    #匹配一个可选的限定词或所有格代名词
           {<NNP>+}                 #匹配一个或多个专有名词
    """
    cp = nltk.RegexpParser(grammar)
    sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"), ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"),
                ("hair", "NN")]
    print(cp.parse(sentence))
    # (S
    #  (NP Rapunzel / NNP)
    # let / VBD
    # down / RP
    # (NP her / PP$ long / JJ golden / JJ hair / NN))
    nouns = [("money", "NN"), ("market", "NN"), ("fund", "NN")]
    grammar = "NP: {<NN><NN>}"  # 匹配两个名词

    # 如果将匹配两个连续名词的文本的规则应用到包含３个连续名词的文本中,则只有前两个名词被分块
    cp = nltk.RegexpParser(grammar)
    print(cp.parse(nouns))
    # (S (NP money/NN market/NN) fund/NN)


def find_chunks(patten='CHUNK: {<V.*> <TO> <V.*>}'):
    cp = nltk.RegexpParser(patten)
    brown = nltk.corpus.brown
    for sent in brown.tagged_sents():
        tree = cp.parse(sent)
        for subtree in tree.subtrees():
            if subtree.label() == 'CHUNK':
                print(subtree)


def demo5():
    find_chunks(patten='NOUNS:{<N.*>{4,}}')


# 简单的加缝器
def demo6():
    grammar = r"""
        NP:
           {<.*>+}      # 匹配所有
           }<VBD|IN>+{  #匹配 VBD或IN 序列
    """
    sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),
                ("the", "DT"), ("cat", "NN")]
    cp = nltk.RegexpParser(grammar)
    print(cp.parse(sentence))


def main():
    demo6()


if __name__ == '__main__':
    main()
