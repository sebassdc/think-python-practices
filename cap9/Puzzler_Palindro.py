# coding=utf-8

__author__ = 'sebassdc'
"""I was driving on the highway the other day and I happened to notice my odometer.
Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000
miles, for example, I’d see 3-0-0-0-0-0.
“Now, what I saw that day was very interesting. I noticed that the last 4 digits were
palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a
palindrome, so my odometer could have read 3-1-5-4-4-5.
“One mile later, the last 5 numbers were palindromic. For example, it could have read
3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And
you ready for this? One mile later, all 6 were palindromic!
“The question is, what was on the odometer when I first looked?

-Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy
    these requirements"""
from time import time


def reverse(string):
    i = len(string) - 1
    stringux = ""
    while True:
        if i < 0:
            break
        stringux += string[i]
        i -= 1
    return stringux


def is_palindrome(string):
    return True if string == reverse(string) else False


def generate_array(n, m):
    aux = []
    for i in range(n, m):
        aux2 = str(i)
        aux.append(aux2)
    return aux


def cond1(string):
    return is_palindrome(string[-4:])


def cond2(string):
    return is_palindrome(string[-5:])

def cond3(string):
    return is_palindrome(string[1:-1])


def cond4(string):
    return is_palindrome(string)


def prueba(array):
    counteroc = 0
    counter = 0
    for i in range(1, len(array)):
        if cond1(array[i]):
            if cond2(array[i+1]):
                if cond3(array[i+2]):
                    if cond4(array[i+3]):
                        return array[i], array[i+1], array[i+2], array[i+3]
    return None

time1 = time()
# Aqui empieza

print prueba(generate_array(100000, 1000000))

# Aqui termina
time2 = time()

print "Defresa: ", time2 - time1