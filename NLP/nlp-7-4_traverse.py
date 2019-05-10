#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-7-4_traverse.py
@Time       : 2019/5/9 15:39
@Version    : 1.0  
@Desc       : None
"""
import nltk


def traverse(t):
    try:
        t.node
    except AttributeError:
        print(t)
    else:
        # Now we know that t.node is defined
        print('(', t.node)
        for child in t:
            traverse(child)
        print(')'),


if __name__ == '__main__':
    tree1 = nltk.Tree('NP', ['Alice'])
    print(tree1)
    tree2 = nltk.Tree('NP', ['the', 'rabbit'])
    print(tree2)
    tree3 = nltk.Tree('VP', ['chased', tree2])
    tree4 = nltk.Tree('S', [tree1, tree3])
    print(tree4)
    print(tree4[1])
    print(tree4[1].label())
    print(tree4.leaves())
    print(tree4[1][1][1])
    # tree3.draw()
    print("====")
    tree = nltk.Tree('(S (NP Alice) (VP chased (NP the rabbit)))')
    traverse(tree)
