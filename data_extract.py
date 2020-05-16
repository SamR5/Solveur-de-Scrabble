#!/usr/bin/python3
# -*- coding: utf-8 -*-

from unidecode import unidecode
import string

file = "Lexique381.txt"

def filtrate(words):
    """Eliminates words containing non-alphabetic characters"""
    fltr = lambda x: '-' not in x and ' ' not in x and "'" not in x and x != ""
    filtrated = list(filter(fltr, words))
    return set(map(lambda x: unidecode(x.lower()), filtrated))

def data_first(data):
    """
    {"a":words starting with a,
     "b":words starting with b,
     "c":...}
    """
    dic = dict()
    for w in data:
        try:
            dic[w[0]].add(w)
        except KeyError:
            dic[w[0]] = {w,}
    return dic

def data_first_two(data):
    """
    {"aa":words starting with aa,
     "ab":words starting with ab,
     "ac":...}
    """
    dic = dict()
    for w in data:
        if len(w) > 1:
            try:
                dic[w[:2]].add(w)
            except KeyError:
                dic[w[:2]] = {w,}
    return dic

def data_last(data):
    """
    {"a":words ending with a,
     "b":words ending with b,
     "c":...}
    """
    dic = dict()
    for w in data:
        try:
            dic[w[-1]].add(w)
        except KeyError:
            dic[w[-1]] = {w,}
    return dic
