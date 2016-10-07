import math


def sqrt(a):
    x = a / 2.0
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
    return x


def test_square_root(a):
    for i in range(1, a + 1):
        a1 = sqrt(float(i))
        a2 = math.sqrt(float(i))
        val = abs(a1 - a2)
        print float(i), "\t", a1, "\t", a2, "\t", val


test_square_root(20)