#!/usr/bin/python3
# -*- coding: utf-8 -*-

#

import itertools as it
import pickle as pk
import string

# loads dictionnaries
with open('data', 'rb') as svg: # a set with all words
    data = pk.loads(svg.read())
# a dict with letters as key and all words beginning by that key as value
with open('data_first', 'rb') as svg:
    dataFirst = pk.loads(svg.read())
# {'aa': words beginning with aa, 'ab': words beginning with 'ab', ... 'zz': 
with open('data_first_two', 'rb') as svg:
    dataFirstTwo = pk.loads(svg.read())
with open('data_last', 'rb') as svg:
    dataLast = pk.loads(svg.read())

def contains(word, letters, s="", e=""):
    """
    Return True if 'word' contains all of 'letters'.
    With 'start' and 'end' restrictions.
    """
    if not word.startswith(s) or not word.endswith(e):
        return False
    # remove the start and end
    if s:
        word = word[len(s):]
    if e:
        word = word[:-len(e)]
    letters = list(letters)
    try:
        for l in word:
            letters.remove(l)
    except:
        return False
    return True

def search_letters(letters, start="", end="", listOfWords=None):
    """
    Return words containing some or all 'letters'
    the data to search in can be limited with listOfWords
    and restricted with start and end.
    """
    words = set()
    if len(start) == 0:
        for pair in it.permutations(set(letters), 2):
            pair = "".join(pair)
            if pair not in dataFirstTwo.keys():
                continue
            for w in dataFirstTwo[pair]:
                if contains(w, letters, e=end):
                    words.add(w)
    elif len(start) == 1:
        for l in letters:
            for w in dataFirst[start]:
                if contains(w, letters, s=start, e=end):
                    words.add(w)
    else:
        try:
            for w in dataFirstTwo[start[:2]]:
                if contains(w, letters, s=start, e=end):
                    words.add(w)
        except KeyError:
            pass
    # from shorter to longer
    return sorted(words, key=len, reverse=True)

def search_end(word):
    """Return all words ending with 'word'"""
    words = []
    for w in dataLast[word[-1]]:
        if w.endswith(word):
            words.append(w)
    return words

def search_start(word):
    """Return all words starting with 'word'"""
    words = []
    if len(word) <= 1:
        for w in dataFirst[word[0]]:
            if w.startswith(word):
                words.append(w)
    else:
        for w in dataFirstTwo[word[:2]]:
            if w.startswith(word):
                words.append(w)
    return words
