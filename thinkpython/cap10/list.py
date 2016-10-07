__author__ = 'sebassdc'


def reverse_string(string):
    i = len(string) - 1
    stringux = ""
    while True:
        if i < 0:
            break
        stringux += string[i]
        i -= 1
    return stringux


def add_list(t):
    tot = 0
    for i in t:
        tot += i
    return tot


def acum_list(t):
    auxlist = []
    for i in range(len(t)):
        auxlist.append(add_list(t[:i + 1]))
    return auxlist


def midle(t):
    return t[1:len(t) - 1]


def chop(t):
    del t[len(t) - 1]
    del t[0]


def is_sorted(t):
    for i in range(1, len(t)):
        if t[i - 1] > t[i]:
            return False
    return True


def has_duplicates(t):
    a = []
    for i in t:
        if i in a:
            return True
        a.append(i)
    return False


def remove_duplicates(t):
    a = []
    for i in t:
        if i in a:
            continue
        else:
            a.append(i)
    return a