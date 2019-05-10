#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author     : ice-melt@outlook.com
@File       : nlp-6-1-sex_identification_errorlist.py
@Time       : 2019/4/23 17:38
@Version    : 1.0  
@Desc       : None
"""
from nltk.corpus import names
import random
import nltk

# 定义一个特征提取器,同时准备一些例子和与其对应的类标签
names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)

train_names = names[1500:]  # 训练模型
devtest_names = names[500:1500]  # 执行错误分析
test_names = names[:500]  # 系统的最终评估


# 函数返回的字典-特征集
def gender_features(word):
    # return {'suffix1': word[-1:]}
    return {'suffix1': word[-1:],
            'suffix2': word[-2:]}


train_set = [(gender_features(n), g) for (n, g) in train_names]
devtest_set = [(gender_features(n), g) for (n, g) in devtest_names]
test_set = [(gender_features(n), g) for (n, g) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)


# 评估
def evaluation(clsfir, tst_set):
    acc = nltk.classify.accuracy(clsfir, tst_set)
    print('测试集的精度为%4f' % acc)
    return acc


evaluation(classifier, devtest_set)

# 使用开发测试集生成分类器在预测名字性别时出现的错误列表
errors = []
for (name, tag) in devtest_names:
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append((tag, guess, name))
for (tag, guess, name) in sorted(errors):
    print('correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name))


# ======================= output ==================================
# ===================== 特征集中使用2个的特征进行训练,结果如下:
# 测试集的精度为0.758000
# correct=female   guess=male     name=Aeriell
# correct=female   guess=male     name=Allyson
# correct=female   guess=male     name=Ambur
# correct=female   guess=male     name=Ardeen
# correct=female   guess=male     name=Ardys
# correct=female   guess=male     name=Ariel
# correct=female   guess=male     name=Arlen
# correct=female   guess=male     name=Arlyn
# correct=female   guess=male     name=Astrix
# correct=female   guess=male     name=Averil
# correct=female   guess=male     name=Ayn
# correct=female   guess=male     name=Beau
# correct=female   guess=male     name=Bel
# correct=female   guess=male     name=Brett
# correct=female   guess=male     name=Brier
# correct=female   guess=male     name=Brigit
# correct=female   guess=male     name=Brooks
# correct=female   guess=male     name=Caitlin
# correct=female   guess=male     name=Carolynn
# correct=female   guess=male     name=Ceil
# correct=female   guess=male     name=Charil
# correct=female   guess=male     name=Charlot
# correct=female   guess=male     name=Chloris
# correct=female   guess=male     name=Ciel
# correct=female   guess=male     name=Coriss
# correct=female   guess=male     name=Cris
# correct=female   guess=male     name=Cristal
# correct=female   guess=male     name=Cybil
# correct=female   guess=male     name=Darell
# correct=female   guess=male     name=Debor
# correct=female   guess=male     name=Delores
# correct=female   guess=male     name=Deloris
# correct=female   guess=male     name=Dot
# correct=female   guess=male     name=Drew
# correct=female   guess=male     name=Emmalyn
# correct=female   guess=male     name=Erinn
# correct=female   guess=male     name=Ethel
# correct=female   guess=male     name=Ethelin
# correct=female   guess=male     name=Ethyl
# correct=female   guess=male     name=Fawn
# correct=female   guess=male     name=Gabriel
# correct=female   guess=male     name=Gen
# correct=female   guess=male     name=Germain
# correct=female   guess=male     name=Gill
# correct=female   guess=male     name=Glynnis
# correct=female   guess=male     name=Gretchen
# correct=female   guess=male     name=Harriet
# correct=female   guess=male     name=Harriott
# correct=female   guess=male     name=Imogen
# correct=female   guess=male     name=Imojean
# correct=female   guess=male     name=Ingaborg
# correct=female   guess=male     name=Inger
# correct=female   guess=male     name=Isador
# correct=female   guess=male     name=Iseabal
# correct=female   guess=male     name=Izabel
# correct=female   guess=male     name=Jacquelyn
# correct=female   guess=male     name=Jessamyn
# correct=female   guess=male     name=Jo
# correct=female   guess=male     name=Jourdan
# correct=female   guess=male     name=Juliet
# correct=female   guess=male     name=Kara-Lynn
# correct=female   guess=male     name=Karel
# correct=female   guess=male     name=Kass
# correct=female   guess=male     name=Katalin
# correct=female   guess=male     name=Katheleen
# correct=female   guess=male     name=Katheryn
# correct=female   guess=male     name=Kerrill
# correct=female   guess=male     name=Kimberlyn
# correct=female   guess=male     name=Koren
# correct=female   guess=male     name=Kristel
# correct=female   guess=male     name=Laurel
# correct=female   guess=male     name=Leanor
# correct=female   guess=male     name=Lilian
# correct=female   guess=male     name=Lust
# correct=female   guess=male     name=Madelon
# correct=female   guess=male     name=Margo
# correct=female   guess=male     name=Marieann
# correct=female   guess=male     name=Marigold
# correct=female   guess=male     name=Marin
# correct=female   guess=male     name=Maryangelyn
# correct=female   guess=male     name=Maryann
# correct=female   guess=male     name=Megan
# correct=female   guess=male     name=Mercedes
# correct=female   guess=male     name=Miriam
# correct=female   guess=male     name=Morgen
# correct=female   guess=male     name=Muffin
# correct=female   guess=male     name=Myriam
# correct=female   guess=male     name=Nell
# correct=female   guess=male     name=Ninon
# correct=female   guess=male     name=Persis
# correct=female   guess=male     name=Quentin
# correct=female   guess=male     name=Rachael
# correct=female   guess=male     name=Rachel
# correct=female   guess=male     name=Rakel
# correct=female   guess=male     name=Raychel
# correct=female   guess=male     name=Rayshell
# correct=female   guess=male     name=Riannon
# correct=female   guess=male     name=Rosamund
# correct=female   guess=male     name=Roselin
# correct=female   guess=male     name=Sal
# correct=female   guess=male     name=Sallyann
# correct=female   guess=male     name=Sam
# correct=female   guess=male     name=Shell
# correct=female   guess=male     name=Sherilyn
# correct=female   guess=male     name=Shirleen
# correct=female   guess=male     name=Sibeal
# correct=female   guess=male     name=Sigrid
# correct=female   guess=male     name=Susan
# correct=female   guess=male     name=Susann
# correct=female   guess=male     name=Thomasin
# correct=female   guess=male     name=Wandis
# correct=male     guess=female   name=Ajay
# correct=male     guess=female   name=Allah
# correct=male     guess=female   name=Alley
# correct=male     guess=female   name=Amery
# correct=male     guess=female   name=Anatole
# correct=male     guess=female   name=Andy
# correct=male     guess=female   name=Arne
# correct=male     guess=female   name=Arvie
# correct=male     guess=female   name=Ashby
# correct=male     guess=female   name=Ashish
# correct=male     guess=female   name=Augie
# correct=male     guess=female   name=Ave
# correct=male     guess=female   name=Barry
# correct=male     guess=female   name=Barty
# correct=male     guess=female   name=Benji
# correct=male     guess=female   name=Berkley
# correct=male     guess=female   name=Bertie
# correct=male     guess=female   name=Brandy
# correct=male     guess=female   name=Broddie
# correct=male     guess=female   name=Brody
# correct=male     guess=female   name=Cary
# correct=male     guess=female   name=Chase
# correct=male     guess=female   name=Che
# correct=male     guess=female   name=Clarance
# correct=male     guess=female   name=Cody
# correct=male     guess=female   name=Cole
# correct=male     guess=female   name=Cy
# correct=male     guess=female   name=Dana
# correct=male     guess=female   name=Danie
# correct=male     guess=female   name=Dickey
# correct=male     guess=female   name=Dickie
# correct=male     guess=female   name=Dougie
# correct=male     guess=female   name=Edie
# correct=male     guess=female   name=Elroy
# correct=male     guess=female   name=Emory
# correct=male     guess=female   name=Ernie
# correct=male     guess=female   name=Farley
# correct=male     guess=female   name=Finley
# correct=male     guess=female   name=Franky
# correct=male     guess=female   name=Frederich
# correct=male     guess=female   name=Gale
# correct=male     guess=female   name=Garvey
# correct=male     guess=female   name=Gary
# correct=male     guess=female   name=Gayle
# correct=male     guess=female   name=Georgia
# correct=male     guess=female   name=Grace
# correct=male     guess=female   name=Graeme
# correct=male     guess=female   name=Guthry
# correct=male     guess=female   name=Hadley
# correct=male     guess=female   name=Harry
# correct=male     guess=female   name=Hasty
# correct=male     guess=female   name=Henry
# correct=male     guess=female   name=Hersh
# correct=male     guess=female   name=Howie
# correct=male     guess=female   name=Hugh
# correct=male     guess=female   name=Ignace
# correct=male     guess=female   name=Isidore
# correct=male     guess=female   name=Jaime
# correct=male     guess=female   name=Jerrie
# correct=male     guess=female   name=Jessie
# correct=male     guess=female   name=Jimmie
# correct=male     guess=female   name=Jose
# correct=male     guess=female   name=Joseph
# correct=male     guess=female   name=Juanita
# correct=male     guess=female   name=Jude
# correct=male     guess=female   name=Lawrence
# correct=male     guess=female   name=Lay
# correct=male     guess=female   name=Lesley
# correct=male     guess=female   name=Leslie
# correct=male     guess=female   name=Levi
# correct=male     guess=female   name=Lonnie
# correct=male     guess=female   name=Mahesh
# correct=male     guess=female   name=Manny
# correct=male     guess=female   name=Marlowe
# correct=male     guess=female   name=Martie
# correct=male     guess=female   name=Merle
# correct=male     guess=female   name=Moise
# correct=male     guess=female   name=Mose
# correct=male     guess=female   name=Munroe
# correct=male     guess=female   name=Nate
# correct=male     guess=female   name=Olle
# correct=male     guess=female   name=Ozzy
# correct=male     guess=female   name=Pattie
# correct=male     guess=female   name=Pearce
# correct=male     guess=female   name=Pembroke
# correct=male     guess=female   name=Pepe
# correct=male     guess=female   name=Percy
# correct=male     guess=female   name=Pierre
# correct=male     guess=female   name=Piggy
# correct=male     guess=female   name=Prentice
# correct=male     guess=female   name=Quincey
# correct=male     guess=female   name=Raleigh
# correct=male     guess=female   name=Ramsey
# correct=male     guess=female   name=Randy
# correct=male     guess=female   name=Ray
# correct=male     guess=female   name=Rich
# correct=male     guess=female   name=Rickey
# correct=male     guess=female   name=Ripley
# correct=male     guess=female   name=Roddie
# correct=male     guess=female   name=Rolfe
# correct=male     guess=female   name=Roscoe
# correct=male     guess=female   name=Samuele
# correct=male     guess=female   name=Scottie
# correct=male     guess=female   name=Shayne
# correct=male     guess=female   name=Sheffy
# correct=male     guess=female   name=Shurlocke
# correct=male     guess=female   name=Sinclare
# correct=male     guess=female   name=Solly
# correct=male     guess=female   name=Stanly
# correct=male     guess=female   name=Temple
# correct=male     guess=female   name=Theodore
# correct=male     guess=female   name=Toddy
# correct=male     guess=female   name=Tracy
# correct=male     guess=female   name=Tre
# correct=male     guess=female   name=Tremayne
# correct=male     guess=female   name=Tuckie
# correct=male     guess=female   name=Verney
# correct=male     guess=female   name=Vinnie
# correct=male     guess=female   name=Walsh
# correct=male     guess=female   name=Ware
# correct=male     guess=female   name=Wesley
# correct=male     guess=female   name=Westleigh
# correct=male     guess=female   name=Willy
# correct=male     guess=female   name=Zach
# correct=male     guess=female   name=Zachary
# correct=male     guess=female   name=Zackariah
# correct=male     guess=female   name=Zary
# correct=male     guess=female   name=Zebedee
# correct=male     guess=female   name=Zechariah
# correct=male     guess=female   name=Zeke
# correct=male     guess=female   name=Zippy
# over!


# ===================== 特征集中使用2个的特征进行训练,结果如下:
# 测试集的精度为0.799000
# correct=female   guess=male     name=Adel
# correct=female   guess=male     name=Adrien
# correct=female   guess=male     name=Ambur
# correct=female   guess=male     name=Anet
# correct=female   guess=male     name=Ansley
# correct=female   guess=male     name=Ardeen
# correct=female   guess=male     name=Ardelis
# correct=female   guess=male     name=Ariel
# correct=female   guess=male     name=Arleen
# correct=female   guess=male     name=Ashleigh
# correct=female   guess=male     name=Ashley
# correct=female   guess=male     name=Aubrey
# correct=female   guess=male     name=Audry
# correct=female   guess=male     name=Babs
# correct=female   guess=male     name=Birgit
# correct=female   guess=male     name=Brandais
# correct=female   guess=male     name=Bridgett
# correct=female   guess=male     name=Brooke
# correct=female   guess=male     name=Caitrin
# correct=female   guess=male     name=Candis
# correct=female   guess=male     name=Chris
# correct=female   guess=male     name=Clem
# correct=female   guess=male     name=Cloris
# correct=female   guess=male     name=Consuelo
# correct=female   guess=male     name=Corabel
# correct=female   guess=male     name=Corliss
# correct=female   guess=male     name=Cris
# correct=female   guess=male     name=Cybill
# correct=female   guess=male     name=Daffy
# correct=female   guess=male     name=Danell
# correct=female   guess=male     name=Daniel
# correct=female   guess=male     name=Darcey
# correct=female   guess=male     name=Dian
# correct=female   guess=male     name=Doralin
# correct=female   guess=male     name=Elizabet
# correct=female   guess=male     name=Elke
# correct=female   guess=male     name=Ethelin
# correct=female   guess=male     name=Evy
# correct=female   guess=male     name=Fan
# correct=female   guess=male     name=Fawn
# correct=female   guess=male     name=Frances
# correct=female   guess=male     name=Francesmary
# correct=female   guess=male     name=Gabey
# correct=female   guess=male     name=Gabriel
# correct=female   guess=male     name=Gail
# correct=female   guess=male     name=Gayleen
# correct=female   guess=male     name=Grethel
# correct=female   guess=male     name=Haleigh
# correct=female   guess=male     name=Harley
# correct=female   guess=male     name=Hazel
# correct=female   guess=male     name=Hildagard
# correct=female   guess=male     name=Hilliary
# correct=female   guess=male     name=Honey
# correct=female   guess=male     name=Ikey
# correct=female   guess=male     name=Iseabal
# correct=female   guess=male     name=Jaleh
# correct=female   guess=male     name=Jerry
# correct=female   guess=male     name=Joey
# correct=female   guess=male     name=Joleen
# correct=female   guess=male     name=Jordain
# correct=female   guess=male     name=Jorry
# correct=female   guess=male     name=Karol
# correct=female   guess=male     name=Kathy
# correct=female   guess=male     name=Kerrin
# correct=female   guess=male     name=Kiley
# correct=female   guess=male     name=Kimberley
# correct=female   guess=male     name=Koo
# correct=female   guess=male     name=Krystal
# correct=female   guess=male     name=Kyrstin
# correct=female   guess=male     name=Laney
# correct=female   guess=male     name=Libby
# correct=female   guess=male     name=Lilyan
# correct=female   guess=male     name=Lind
# correct=female   guess=male     name=Linet
# correct=female   guess=male     name=Loren
# correct=female   guess=male     name=Lucky
# correct=female   guess=male     name=Lurleen
# correct=female   guess=male     name=Madlin
# correct=female   guess=male     name=Magdalen
# correct=female   guess=male     name=Maisey
# correct=female   guess=male     name=Marabel
# correct=female   guess=male     name=Marion
# correct=female   guess=male     name=Megan
# correct=female   guess=male     name=Meghan
# correct=female   guess=male     name=Mel
# correct=female   guess=male     name=Melisent
# correct=female   guess=male     name=Mellisent
# correct=female   guess=male     name=Michel
# correct=female   guess=male     name=Norean
# correct=female   guess=male     name=Oliy
# correct=female   guess=male     name=Pat
# correct=female   guess=male     name=Pegeen
# correct=female   guess=male     name=Persis
# correct=female   guess=male     name=Pet
# correct=female   guess=male     name=Philis
# correct=female   guess=male     name=Phillis
# correct=female   guess=male     name=Phylis
# correct=female   guess=male     name=Pooh
# correct=female   guess=male     name=Pris
# correct=female   guess=male     name=Raf
# correct=female   guess=male     name=Rakel
# correct=female   guess=male     name=Rey
# correct=female   guess=male     name=Robin
# correct=female   guess=male     name=Rosamond
# correct=female   guess=male     name=Rosario
# correct=female   guess=male     name=Scarlet
# correct=female   guess=male     name=Sean
# correct=female   guess=male     name=Shamit
# correct=female   guess=male     name=Shannen
# correct=female   guess=male     name=Shaun
# correct=female   guess=male     name=Sheelagh
# correct=female   guess=male     name=Shel
# correct=female   guess=male     name=Shelagh
# correct=female   guess=male     name=Sherry
# correct=female   guess=male     name=Shir
# correct=female   guess=male     name=Shirley
# correct=female   guess=male     name=Sibel
# correct=female   guess=male     name=Sydney
# correct=female   guess=male     name=Tamar
# correct=female   guess=male     name=Tuesday
# correct=female   guess=male     name=Ulrike
# correct=female   guess=male     name=Val
# correct=female   guess=male     name=Vikky
# correct=female   guess=male     name=Winnifred
# correct=female   guess=male     name=Yoko
# correct=female   guess=male     name=Zoe
# correct=male     guess=female   name=Alfonse
# correct=male     guess=female   name=Anatole
# correct=male     guess=female   name=Andrea
# correct=male     guess=female   name=Angie
# correct=male     guess=female   name=Archie
# correct=male     guess=female   name=Ari
# correct=male     guess=female   name=Augie
# correct=male     guess=female   name=Ave
# correct=male     guess=female   name=Avi
# correct=male     guess=female   name=Barnie
# correct=male     guess=female   name=Barth
# correct=male     guess=female   name=Caryl
# correct=male     guess=female   name=Chaddie
# correct=male     guess=female   name=Chaddy
# correct=male     guess=female   name=Clayborne
# correct=male     guess=female   name=Dale
# correct=male     guess=female   name=Demetre
# correct=male     guess=female   name=Donny
# correct=male     guess=female   name=Elijah
# correct=male     guess=female   name=Etienne
# correct=male     guess=female   name=Felix
# correct=male     guess=female   name=Frankie
# correct=male     guess=female   name=Franklyn
# correct=male     guess=female   name=Freddie
# correct=male     guess=female   name=Garcia
# correct=male     guess=female   name=Georg
# correct=male     guess=female   name=Georgia
# correct=male     guess=female   name=Gere
# correct=male     guess=female   name=Giffie
# correct=male     guess=female   name=Grace
# correct=male     guess=female   name=Guthrie
# correct=male     guess=female   name=Hari
# correct=male     guess=female   name=Henrie
# correct=male     guess=female   name=Herve
# correct=male     guess=female   name=Hodge
# correct=male     guess=female   name=Jamie
# correct=male     guess=female   name=Kenny
# correct=male     guess=female   name=Kingsly
# correct=male     guess=female   name=Kyle
# correct=male     guess=female   name=Laurance
# correct=male     guess=female   name=Lemmy
# correct=male     guess=female   name=Llewellyn
# correct=male     guess=female   name=Lorne
# correct=male     guess=female   name=Lorrie
# correct=male     guess=female   name=Maurise
# correct=male     guess=female   name=Meredith
# correct=male     guess=female   name=Montague
# correct=male     guess=female   name=Morlee
# correct=male     guess=female   name=Nevile
# correct=male     guess=female   name=Niki
# correct=male     guess=female   name=Ole
# correct=male     guess=female   name=Pace
# correct=male     guess=female   name=Paige
# correct=male     guess=female   name=Pryce
# correct=male     guess=female   name=Rabbi
# correct=male     guess=female   name=Reggy
# correct=male     guess=female   name=Roddy
# correct=male     guess=female   name=Roth
# correct=male     guess=female   name=Rudy
# correct=male     guess=female   name=Scotti
# correct=male     guess=female   name=See
# correct=male     guess=female   name=Sergei
# correct=male     guess=female   name=Slade
# correct=male     guess=female   name=Tally
# correct=male     guess=female   name=Tanny
# correct=male     guess=female   name=Tommy
# correct=male     guess=female   name=Torrance
# correct=male     guess=female   name=Towny
# correct=male     guess=female   name=Tracy
# correct=male     guess=female   name=Tyrone
# correct=male     guess=female   name=Vite
# correct=male     guess=female   name=Waine
# correct=male     guess=female   name=Waite
# correct=male     guess=female   name=Wayne
# correct=male     guess=female   name=Zechariah

print("over!")
