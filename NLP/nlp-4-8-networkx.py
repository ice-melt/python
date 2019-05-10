#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt
@File       : nlp-4-8-networkx.py
@Time       : 2019/4/18 17:46
@Version    : 1.0  
@Desc       : None
"""
import networkx as nx
import matplotlib
from nltk.corpus import wordnet as wn


def traverse(g, start, node):
	g.depth[node.name] = node.shortest_path_distance(start)
	for child in node.hyponyms():
		g.add_edge(node.name, child.name)
		traverse(g, start, child)


def hyponym_graph(start):
	g = nx.Graph()
	g.depth = {}
	traverse(g, start, start)
	return g


def graph_draw(g):
	nx.draw(
		g,
		node_size=[16 * g.degree(n) for n in g],
		node_color=[g.depth[n] for n in g],
		with_labels=False
	)
	matplotlib.pyplot.show()


dog = wn.synset('dog.n.01')
graph = hyponym_graph(dog)
graph_draw(graph)
