from math import gcd


def kasiski(text):
    distances = []
    for size in (4, 5):
        for i in range(len(text) - size):
            sub = text[i : i + size]
            for j in range(i + size, len(text) - size):
                if sub == text[j : j + size]:
                    distances.append(j - i)

    if not distances:
        return None

    g = distances[0]
    for num in distances:
        g = gcd(num, g)
    return g

#find key lenghts from compute gcd of distance between repeated letter combinations from 4 letters to avoid random coincidences