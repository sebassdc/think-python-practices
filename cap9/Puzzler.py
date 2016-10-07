# coding=utf-8
__author__ = 'sebassdc'

"""Give me a word with three consecutive double letters. I’ll give you a couple of words
that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-
p-p-i. If you could take out those i’s it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.
Of course there are probably 500 more but I can only think of one. What is the word?"""


def is_3_double_letters(wordx):
    counter = 0
    falses = 0
    for i in range(1, len(wordx)):
        if wordx[i] == wordx[i-1]:
            counter += 1
            falses = 0
            if counter == 3:
                return True
        else:
            falses += 1
            if falses == 2:
                return False
    return False


fin = open('words.txt')
tot = 0
we = 0
for line in fin:
    tot += 1
    word = line.strip()
    if is_3_double_letters(word):
        we += 1
        print word
porcentaje = (float(we)/tot) * 100
print porcentaje
