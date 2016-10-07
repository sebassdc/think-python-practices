def uses_all(w, s):
    return use_only(s, w)


def avoid(w, s):
    for i in w:
        if i in s:
            return False
    return True


def use_only(w, s):
    for i in w:
        if i not in s:
            return False
    return True


def has_no_e(w):
    return avoid(w, "e")


fin = open('words.txt')
tot = 0
we = 0
without_e = []
for line in fin:
    tot += 1
    word = line.strip()
    if uses_all(word, "aeiou"):
        we += 1
        print word

porcentaje = (float(we) / tot) * 100
print porcentaje
