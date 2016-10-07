__author__ = 'sebassdc'
from ROT13 import *


def is_rotate_pair(a, b):
    for i in range(1, 27):
        if b == rotate(a, i):
            return True
    return False


def make_word_list():
    """Reads lines from a file and builds a list using append."""
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def has_duplicates(t):
    d = dict()
    for i in t:
        if i in d:
            return True
        else:
            d[i] = i
    return False


word_list = make_word_list()
cache = dict()

