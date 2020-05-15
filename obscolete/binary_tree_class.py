#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
#
 
import random as r
import time as t
 
class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
 
    def insert(self, value):
        global doublon
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = Node(value)
        elif value > self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = Node(value)
        else:
            print(value)
            doublon += 1
 
    def search(self, value):
        if self.value == value:
            return True
        elif value > self.value:
            if self.right is not None:
                return self.right.search(value)
        else:
            if self.left is not None:
                return self.left.search(value)
        return False
 
def f(x):
    for i in x:
        if ord(i) not in range(ord('a'), ord('z')+1):
            return False
    return True
 
def main():
    with open("lexique.txt", "r") as txt:
        data = [i.lower()[:-1] for i in txt.readlines()]
    return sorted(filter(f, data))
 
def bin_part(array, low, upp):
    global TREE
    mid = (low+upp)//2
    if low==mid or mid==upp:
        #TREE.insert(array[low]) # this is a duplicate
        return
    TREE.insert(array[mid])
    bin_part(array, low, mid)
    bin_part(array, mid, upp)
   
 
def binarize(words):
    global TREE
    words.sort()
    lower, upper = 0, len(words)
    middle = (lower+upper)//2
    TREE = Node(words[middle])
    bin_part(words, lower, middle)
    bin_part(words, middle, upper)
    TREE.insert(words[lower])
    TREE.insert(words[upper-1])
 
def is_balanced(n, dep=1):
    global depths
    if n.left is None or n.right is None:
        depths.add(dep)
    else:
        try:
            is_balanced(n.left, dep+1)
        except:
            pass
        try:
            is_balanced(n.right, dep+1)
        except:
            pass
 
def checkspeed():
    results = []
    for i in range(20):
        w = r.choice(data)
        t0 = t.time()
        for i in range(50):
            a = w in data
        t1 = t.time()
        for i in range(50):
            b = TREE.search(w)
        t2 = t.time()
        results.append((round(t1-t0, 4), round(t2-t1, 4)))
        if a!=b:
            print("Error", w)
            return
    return results
 
if __name__ == "__main__":
    data = main()
    TREE = None
    doublon = 0
    binarize(data)
    for i in checkspeed():
        print(i)
    depths = set()
    is_balanced(TREE)
    print(max(depths)-min(depths))
