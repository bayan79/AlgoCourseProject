#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re #регулярные выражения
from random import uniform #вещест числа в пределах
from collections import defaultdict #словарь со значениями по умолчанию

r_alphabet = re.compile(u'[а-яА-Я0-9-]+|[.,:;?!]+')

def to_strings(textfile):
    data = open(textfile, encoding='utf-8')
    for string1 in data:
        yield string1

def to_words(strings):
    for string1 in strings:
        for word in r_alphabet.findall(string1):
            yield word

def to_trigrams(words): #последовательности из 3 слов подряд
    w0, w1 = '$', '$'
    for w2 in words:
        yield w0, w1, w2
        if w2 in '.!?':
            yield w1, w2, '$'
            yield w2, '$','$'
            w0, w1 = '$', '$'
        else:
            w0, w1 = w1, w2

def train(textfile):
    strings = to_strings(textfile)
    words = to_words(strings)
    trigrams = to_trigrams(words)
    bi, tri = defaultdict(lambda: 0.0), defaultdict(lambda: 0.0)

    for w0, w1, w2 in trigrams:
        bi[w0, w1] += 1
        tri[w0, w1, w2] += 1

    examle = {} #слово : вероятность
    for (w0, w1, w2), freq in tri.items():
        if (w0, w1) in examle:
            examle[w0, w1].append((w2, freq/bi[w0, w1])) #вероятность слова в зависимости от двух предыдущих
        else:
            examle[w0, w1] = [(w2, freq/bi[w0, w1])]
    return examle

def new_sentence(examle):
    phrase = ''
    w0, w1 = '$', '$'
    while 1: #while wi != '$'
        w0, w1 = w1, unirand(examle[w0, w1])
        if w1 == '$': break
        if w1 in ('.!?,;:') or w0 == '$':
            phrase += w1
        else:
            phrase += ' ' + w1
    return phrase.capitalize()

def unirand(seq): #выбор первого слова с равной вероятностью
    sum_, freq_ = 0, 0
    for item, freq in seq:
        sum_ += freq
    rnd = uniform(0, sum_)
    for token, freq in seq:
        freq_ += freq
        if rnd < freq_:
            return token


example = train('LevNikolaich.txt')
for i in range(10):
    print (new_sentence(example))



# Вывод:
# Масонство -это они-то и могли быть известны кому-нибудь из нашей армии слухи.
# Я за долохова!
# Он видел, что это было с ним было, ежели бы у суворова руки свободны были; только сила и бодрость жизни во всех чертах ее, посадил на средний диван.
# - позабавьтесь от скуки сблизиться и беседовать с любочкой ехать на праздник, он, наконец, сам себе, перечел письма иосифа алексеевича.
# Нет, это то, что этими именно, и из приезжавших к ним пьер не видал его князь андрей.
# Блеск утра был волшебный.
# Да, граф и графиня писала письмо сыну.
# По вступлении таким образом в бой будут даны приказания, делающего возможным исполнение последнего.