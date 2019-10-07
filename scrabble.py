#!/usr/bin/python3
# -*- coding: utf-8 -*-

#

import sys
import tkinter as tk
import string
import searchword as sw

class Scrabble():
    """"""
    def __init__(self, master):
        self.master = master
        self.gui()

    def gui(self):
        """"""
        self.userLetters = tk.StringVar()
        self.userLetters.set('bateau')
        self.freeLetters = tk.StringVar() # letters free on the board
        self.startsWith = tk.StringVar()
        self.endsWith = tk.StringVar()

        self.userLLabel = tk.Label(self.master, text="Letters in hand")
        self.userLEntry = tk.Entry(self.master, textvariable=self.userLetters)
        self.userLLabel.grid(row=0, column=0, sticky='w', padx=5)
        self.userLEntry.grid(row=0, column=1, padx=5, pady=5)
        
        self.freeLLabel = tk.Label(self.master, text="Free letters on board")
        self.freeLEntry = tk.Entry(self.master, textvariable=self.freeLetters)
        self.freeLLabel.grid(row=1, column=0, sticky='w', padx=5)
        self.freeLEntry.grid(row=1, column=1, padx=5, pady=5)
        
        self.startsWLabel = tk.Label(self.master, text="Letters to begin with")
        self.startsWEntry = tk.Entry(self.master, textvariable=self.startsWith)
        self.startsWLabel.grid(row=2, column=0, sticky='w', padx=5)
        self.startsWEntry.grid(row=2, column=1, padx=5, pady=5)
        
        self.endsWLabel = tk.Label(self.master, text="Letters to end with")
        self.endsWEntry = tk.Entry(self.master, textvariable=self.endsWith)
        self.endsWLabel.grid(row=3, column=0, sticky='w', padx=5)
        self.endsWEntry.grid(row=3, column=1, padx=5, pady=5)

        self.searchB = tk.Button(self.master, text="Search",
                                 command=self.search)
        self.searchB.grid(row=4, columnspan=2)

        self.result = tk.Listbox(self.master)
        self.result.grid(row=5, columnspan=2, pady=5)
        
    def search(self):
        """Search for words according to user entries"""
        u = self.userLetters.get().lower().replace(" ", "")
        e = self.endsWith.get().lower().replace(" ", "")
        s = self.startsWith.get().lower().replace(" ", "")
        f = self.freeLetters.get().lower().replace(" ", "")
        # if there is at least one non ascii char (special, digit...)
        # acts like nothing is found
        if any(i not in string.ascii_lowercase for i in u + e + s + f):
            return []
        # first it search all words with the user's end restriction
        ends = set(sw.search_end(e)) if e is not "" else set()
        # then all words with the user's start restriction
        starts = set(sw.search_start(s)) if s is not "" else set()
        # intersection of the two except if one is empty
        if len(ends) == 0:
            wordsFound = starts
        elif len(starts) == 0:
            wordsFound = ends
        else:
            wordsFound = starts & ends
        # if wordsFound is None in search_letters, it will search
        # throught the whole dictionary
        if len(wordsFound) == 0:
            wordsFound = None
        
        f = "".join(set(f))
        found = set()
        if f is not "": # if there are some free letters on the board
            for char in f:
                if char not in string.ascii_lowercase:
                    continue
                # only search in the words we already found
                found.update(sw.search_letters(u + char, s, e, wordsFound))
        else:
            found.update(sw.search_letters(u, s, e, wordsFound))
        # sort by lexicographical order and after by length
        return self.update_results(sorted(found))


    def update_results(self, wordsFound):
        self.result.delete(0, tk.END)
        for ind, w in enumerate(sorted(wordsFound, key=len,
                                       reverse=True)):
            self.result.insert(ind, w)
        
                
                
if __name__ == "__main__":
    root = tk.Tk()
    app = Scrabble(root)
    root.mainloop()
