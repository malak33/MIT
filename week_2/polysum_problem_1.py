import math


def polysum(n, s):
    a = 0.25 * n * s ** 2 / math.tan(math.pi/n)
    p = ((n * s) ** 2)
    total = a + p
    return round(total, 4)

print(polysum(17, 96))

