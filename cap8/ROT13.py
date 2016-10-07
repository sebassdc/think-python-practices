

def rotate_letter(c, n):
    codletra = ord(c)
    if c.islower():
        a, b = 123, 97
    else:
        a, b = 91, 65
    codletra += n
    if codletra > a:
        codletra -= 26
    if codletra < b:
        codletra += 26
    return chr(codletra)


def rotate(s, n):
    aux = ''
    for i in s:
        aux += rotate_letter(i, n)
    return aux
