__author__ = 'sebassdc'


def is_anagram(test, original):
    test = test.lower().replace(" ", "")
    original = original.lower().replace(" ", "")
    if sorted(test) == sorted(original):
        return True
    else:
        return False


def sumall(*t):
    acum = 0
    for i in t:
        acum += i
    return acum


def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False


def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def gen_text(filename):
    s = ""
    fin = open(filename)
    for i in fin:
        s += i.strip()
    return s


def make_word_list():
    """Reads lines from a file and builds a list using append."""
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def most_frecuent(s):
    s.strip()
    d = dict()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    d = invert_dict(d)
    llaves = d.keys()
    llaves.sort(reverse=True)
    for i in llaves:
        print i, "\t", d[i]


def set_anagrams(lista):
    d = dict()
    d2 = dict()
    for elemento in lista:
        llave = "".join(sorted(elemento))
        if llave in d:
            d[llave].append(elemento)
        else:
            d[llave] = [elemento]

    for llave in d.keys():
        if len(d[llave]) == 1:
            d.pop(llave)
    return d


def sort_by_length(elements):
    t = []
    for elemento in elements:
        t.append((len(elemento), elemento))

    t.sort(reverse=True)

    res = []
    for length, elemento in t:
        res.append(elemento)
    return res


def keep_data(filename, data):
    fin = open(filename, 'w')
    for i in data:
        fin.write(str(i) + "\r\n")
    fin.close()
    print "HECHO"


lista = make_word_list()
diccionario = set_anagrams(lista)
valores = diccionario.values()
valores = sort_by_length(valores)

for i in valores:
    if len(i[0]) == 8:
        print i