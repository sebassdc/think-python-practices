import math


def check_fermat(a, b, c, n):
    if(a**n)+(b**n) == c**n:
        check = True
    else:
        check = False

    if n > 2 and check:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work"

def userInterface():
    a = int(input("Ingresa el valor de 'a': "))
    b = int(input("Ingresa el valor de 'b': "))
    c = int(input("Ingresa el valor de 'c': "))
    n = int(input("Ingresa el valor de 'n': "))
    check_fermat(a, b, c, n)

userInterface()