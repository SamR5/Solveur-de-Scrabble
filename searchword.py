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

def search(word):
    """Return True if word is in data"""
    return word in data[word[0]]

def search_letters(letters, start="", end="", listOfWords=None):
    """
    Return words containing all permutations of 'letters'
    the data to search in can be limited with listOfWords
    and restricted with start and end.
    """
    if len(letters) <= 1:
        return []
    words = set()
    maxi = len(letters)+1 if len(letters)+1 < 26 else 26
    for i in range(2, maxi):
        for perm in it.permutations(letters, i):
            perm = start + "".join(perm) + end
            # search in the words that begins by the same letter
            if listOfWords is None:
                if perm[:2] not in dataFirstTwo:
                    continue
                if perm in dataFirstTwo[perm[:2]]:
                    words.add(perm)
            else:
                if perm in listOfWords:
                    words.add(perm)
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
