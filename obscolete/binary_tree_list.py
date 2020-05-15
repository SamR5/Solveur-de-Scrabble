#!/usr/bin/python3
# -*- coding: utf-8 -*-

def insert(tree, value, index=0):
    if tree[index] is None:
        tree[index] = value
        return tree
    left, right = 2*index+1, 2*index+2
    if value < tree[index]:
        tree = insert(tree, value, left)
    elif value > tree[index]:
        tree = insert(tree, value, right)
    return tree
 
def search(tree, value):
    index = 0
    while tree[index] != value:
        if value < tree[index]:
            index = 2*index + 1
        else:
            index = 2*index + 2
        if index >= len(tree) or tree[index] is None:
            return False
    return True

def bin_part(array, tree, low, upp):
    mid = (low+upp)//2
    if low==mid or mid==upp:
        return tree
    tree = insert(tree, array[mid])
    tree = bin_part(array, tree, low, mid)
    tree = bin_part(array, tree, mid, upp)
    return tree
   
 
def binarize(words):
    words.sort()
    lower, upper = 0, len(words)
    middle = (lower+upper)//2
    tree = [None] * len(words)*2
    tree[0] = words[middle]
    bin_part(words, tree, lower, middle)
    bin_part(words, tree, middle, upper)
    tree = insert(tree, words[lower])
    tree = insert(tree, words[upper-1])
    return tree

