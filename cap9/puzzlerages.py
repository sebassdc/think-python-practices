__author__ = 'sebassdc'
"""
Necesito 8 numeros de 2 digitos que:
-Al revertirse sean equidistantes"""
from time import time
from Puzzler_Palindro import reverse, generate_array




time1 = time()
# Aqui empieza

array = generate_array(10, 100)
arrayaux = []
for elemento in array:
    ele = int(reverse(elemento)) - int(elemento)
    if ele < 15 or ele > 70:
        continue
    arrayaux.append((elemento, reverse(elemento) , ele))

count = 0
for i in arrayaux:
    if i[2] == 18:
        count += 1

print count
print arrayaux
# Aqui termina
time2 = time()

print "Defresa: ", time2 - time1
