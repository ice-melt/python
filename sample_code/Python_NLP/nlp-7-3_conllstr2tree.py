#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-7-3_conllstr2tree.py
@Time       : 2019/5/9 9:19
@Version    : 1.0  
@Desc       : None
"""
import nltk
from nltk.corpus import conll2000


def conllstr2tree():
    text = '''
    he PRP B-NP
    accepted VBD B-VP
    the DT B-NP
    position NN I-NP
    of IN B-PP
    vice NN B-NP
    chairman NN I-NP
    of IN B-PP
    Carlyle NNP B-NP
    Group NNP I-NP
    , , O
    a DT B-NP
    merchant NN I-NP
    banking NN I-NP
    concern NN I-NP
    . . O
    '''
    nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw()


def chunked_sents():
    print(conll2000.chunked_sents('train.txt')[99])
    # (S
    #   (PP Over/IN)
    #   (NP a/DT cup/NN)
    #   (PP of/IN)
    #   (NP coffee/NN)
    #   ,/,
    #   (NP Mr./NNP Stone/NNP)
    #   (VP told/VBD)
    #   (NP his/PRP$ story/NN)
    #   ./.)
    print(conll2000.chunked_sents('train.txt', chunk_types=['NP'])[99])
    # (S
    #   Over/IN
    #   (NP a/DT cup/NN)
    #   of/IN
    #   (NP coffee/NN)
    #   ,/,
    #   (NP Mr./NNP Stone/NNP)
    #   told/VBD
    #   (NP his/PRP$ story/NN)
    #   ./.)

def main():
    chunked_sents()


if __name__ == '__main__':
    main()
