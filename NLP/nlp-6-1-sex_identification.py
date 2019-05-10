#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-6-1-sex_identification.py
@Time       : 2019/4/23 10:09
@Version    : 1.0  
@Desc       : None
"""


# 函数返回的字典-特征集
def gender_features(word):
    return {'last_letter': word[-1]}
    # return {'last_letter': word[-1], 'first_letter': word[0], 'lenth': len(word)}


# def gender_features(name):
#     features = dict()
#     features["firstletter"] = name[0].lower()
#     features["lastletter"] = name[-1].lower()
#     for letter in 'abcdefghigklmnopqrstuvwxyz':
#         features["count(%s)" % letter] = name.lower().count(letter)
#         features["has(%s)" % letter] = (letter in name.lower())
#     return features


gf = gender_features('Jonh')
print(gf)


def predict(clsfir, nm):
    lbl = clsfir.classify(gender_features(nm))
    print('%s预测为%s' % (nm, lbl))
    return lbl


from nltk.corpus import names
import random
import nltk

# 定义一个特征提取器,同时准备一些例子和与其对应的类标签
names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)

featuresets = [(gender_features(n), g) for (n, g) in names]
train_set, test_set = featuresets[500:], featuresets[:500]
# 贝叶斯分类器训练
classifier = nltk.NaiveBayesClassifier.train(train_set)
# 预测
predict(classifier, 'Neo')
predict(classifier, 'Trinity')


# 评估
def evaluation(clsfir, tst_set):
    acc = nltk.classify.accuracy(clsfir, tst_set)
    print('测试集的精度为%4f' % acc)
    return acc


evaluation(classifier, test_set)

# 分析
classifier.show_most_informative_features(5)

# ======================= output ==================================
# ===================== 特征集中使用简单的特征进行训练,结果如下:
# {'last_letter': 'h'}
# Neo预测为male
# Trinity预测为female
# 测试集的精度为0.784000
# Most Informative Features
#              last_letter = 'a'            female : male   =     35.8 : 1.0
#              last_letter = 'k'              male : female =     31.2 : 1.0
#              last_letter = 'f'              male : female =     15.9 : 1.0
#              last_letter = 'p'              male : female =     11.2 : 1.0
#              last_letter = 'd'              male : female =      9.9 : 1.0
# over!

# ===================== 特征集中包含大量的指定特征,结果如下:
# {'firstletter': 'j', 'lastletter': 'h', 'count(a)': 0, 'has(a)': False, 'count(b)': 0, 'has(b)': False, 'count(c)': 0, 'has(c)': False, 'count(d)': 0, 'has(d)': False, 'count(e)': 0, 'has(e)': False, 'count(f)': 0, 'has(f)': False, 'count(g)': 0, 'has(g)': False, 'count(h)': 1, 'has(h)': True, 'count(i)': 0, 'has(i)': False, 'count(k)': 0, 'has(k)': False, 'count(l)': 0, 'has(l)': False, 'count(m)': 0, 'has(m)': False, 'count(n)': 1, 'has(n)': True, 'count(o)': 1, 'has(o)': True, 'count(p)': 0, 'has(p)': False, 'count(q)': 0, 'has(q)': False, 'count(r)': 0, 'has(r)': False, 'count(s)': 0, 'has(s)': False, 'count(t)': 0, 'has(t)': False, 'count(u)': 0, 'has(u)': False, 'count(v)': 0, 'has(v)': False, 'count(w)': 0, 'has(w)': False, 'count(x)': 0, 'has(x)': False, 'count(y)': 0, 'has(y)': False, 'count(z)': 0, 'has(z)': False}
# Neo预测为male
# Trinity预测为female
# 测试集的精度为0.772000
# Most Informative Features
#               lastletter = 'a'            female : male   =     35.7 : 1.0
#               lastletter = 'k'              male : female =     30.8 : 1.0
#               lastletter = 'f'              male : female =     17.3 : 1.0
#               lastletter = 'p'              male : female =     11.9 : 1.0
#               lastletter = 'v'              male : female =     11.2 : 1.0
# over!

print("over!")
