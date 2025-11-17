from collections import Counter
from en_freq import en_freqs

def hi_square(text):
    cnt = Counter(text)
    x2 = 0
    for let, freq in en_freqs.items():
        O = cnt.get(let, 0)
        E = len(text) * freq
        x2 += (O - E) ** 2 / E
    return x2

#hi square statisticks allowing to evalute similarity with normal english text, then smaller value then greater the match