'''
I created this program as a part of my COP 1000 class.
It provides an example of removing a single entry in a list,
by comparing the entry to be removed, with the entry in the list.

Created By: Austin Garrett (MetaRollover)
'''



stringyString = "Funk"
listyList = ["Funk","Soul","Brother","Right","About","Now"]


def myRemove(stringy,listy):
    l = 0
    for mark in listy:
        if mark == stringy:
            del listy[l]
            l = l + 1
        else:
            l = l + 1
    print(listy)

myRemove(stringyString,listyList)
