#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import pickle as pk
from unidecode import unidecode
import string

file = "Lexique381.txt"

def filtrate(words):
    "Filtrate and restructure the data"
    fltr = lambda x: '-' not in x and ' ' not in x and "'" not in x
    filtrated = list(filter(fltr, words))
    return set(map(unidecode, filtrated))

def data_first(data):
    """{"a":wordsStartingWithA, "b":wordsStartingWithB, "c":...}"""
    return {i:{j for j in data if j.startswith(i)}
              for i in string.ascii_lowercase}

def data_first_two(data):
    """{"aa":wordsStartingWithAa, "ab":wordsStartingWithAb, "ac":...}"""
    dic = {"".join([i, j]):{k for k in data if k.startswith(i+j)}
           for i in string.ascii_lowercase
           for j in string.ascii_lowercase}
    toDel = []
    for k, v in dic.items():
        if len(v) == 0:
            toDel.append(k)
    for i in toDel:
        del dic[i]
    return dic

def data_last(data):
    """{"a":wordsEndingWithA, "b":wordsEndingWithB, "c":...}"""
    dic = {i:{j for j in data if j.endswith(i)}
                for i in string.ascii_lowercase}
    toDel = []
    for k, v in dic.items():
        if len(v) == 0:
            toDel.append(k)
    for i in toDel:
        del dic[i]
    return dic

if __name__ == "__main__":
    with open("lexique.txt", 'r') as lxq:
        words = lxq.read().split('\n')
    data = filtrate(words)
    
    with open('data', 'wb') as svg:
        mypick = pk.Pickler(svg)
        mypick.dump(data)

    with open('data_first', 'wb') as svg:
        mypick = pk.Pickler(svg)
        mypick.dump(data_first(data))

    with open('data_first_two', 'wb') as svg:
        mypick = pk.Pickler(svg)
        mypick.dump(data_first_two(data))

    with open('data_last', 'wb') as svg:
        mypick = pk.Pickler(svg)
        mypick.dump(data_last(data))
