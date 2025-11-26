from math import gcd
from sympy import isprime

def kasiski(text):
    distances = []
    for size in (3, 4, 5, 6):
        for i in range(len(text) - size):
            sub = text[i : i + size]
            for j in range(i + size, len(text) - size):
                if sub == text[j : j + size]:
                    distances.append(j - i)

    if not distances:
        return None

    dist_i = [x for x in distances if not (isprime(x) and x > 9)]
    g = min(dist_i)

    for num in distances:
        if gcd(num, g) <= 9 and gcd(num, g) != 1 and gcd(num, g) != 2:
            g = gcd(num, g)
    return g


# find key lenghts from compute gcd of distance between repeated letter combinations from 4 letters to avoid random coincidences

