__author__ = 'sebassdc'
from list import *


list = ['amor', 'roma', 'cosa', 'pato', 'olakase', 'otap']


aux = []
for i in list:
    if reverse_string(i) in list:
        aux.append(i)


print(aux)