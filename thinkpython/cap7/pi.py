import math


def f(n):
    return math.factorial(n)


def aprox_pi():
    const = (2 * math.sqrt(2)) / 9801
    suma = 0
    k = 0
    while True:

        a = f(4 * k) * (1103 + 26390 * k)
        b = (f(k)**4) * (396**(4 * k))
        por = a / b
        suma += por
        if por < 1e-15:
            break
        k += 1
    return const * suma


inversepi = aprox_pi()
print 1/inversepi, "\t", "Srinivasa Ramanujan"
print math.pi, "\t", "Original"