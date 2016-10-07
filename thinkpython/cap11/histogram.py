
known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def reverse_lookup(d, v):
    auxl = []
    for k in d:
        if d[k] == v:
            auxl.append(k)
    return auxl


def print_hist(hist):
    lista = hist.keys()
    lista.sort()
    for c in lista:
        print c, hist[c]


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

for i in range(100):
    print "%d\t%d" % (i, fibonacci(i))
