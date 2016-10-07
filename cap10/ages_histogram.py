__author__ = 'sebassdc'
from list import has_duplicates, add_list
import random
import time


def promedio(t):
    aux = add_list(t)
    return aux / float(len(t))


def prueba(a):
    students = []
    for i in range(a):
        students.append(random.randint(1, 365))
    return has_duplicates(students)


def histograma():
    values = []
    matches = 0
    no_matches = 0
    for i in range(1000):
        values.append(prueba(23))
    for i in values:
        if i:
            matches += 1
        else:
            no_matches += 1
    matches_percent = (matches / 1000.0) * 100
    no_matches_percent = (no_matches/1000.0) * 100
    return matches_percent, no_matches_percent


tiempo1 = time.time()
ma = []
noma = []
for i in range(1000):
    aux = histograma()
    ma.append(aux[0])
    noma.append(aux[1])

print promedio(ma), promedio(noma)
tiempo2 = time.time()

print "Tiempo total: ", tiempo2 - tiempo1
