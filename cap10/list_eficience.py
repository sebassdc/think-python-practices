__author__ = 'sebassdc'
from time import time


def append_list():
    a = []
    fin = open('words.txt')
    for i in fin:
        a.append(i)
    fin.close()


def sum_list():
    a = []
    fin = open('words.txt')
    for i in fin:
        a += [i]
    fin.close()


tiempo1 = time()
append_list()
tiempo2 = time()
print "append_list() dura: %f segundos" % (tiempo2 - tiempo1)

tiempo1 = time()
sum_list()
tiempo2 = time()
print "sum_list() dura: %f segundos" % (tiempo2 - tiempo1)
