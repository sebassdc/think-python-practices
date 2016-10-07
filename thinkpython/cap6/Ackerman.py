
def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        aux = ack(m, n-1)
        return ack(m - 1, aux)


print ack(2, 2)
print ack(2, 3)
print ack(3, 6)
