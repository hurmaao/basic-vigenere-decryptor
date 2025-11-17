from caesar import caesar_crypt
from hi2 import hi_square

def find_key(text, len_key):
    crypt_all = []
    crypt_by_one_symb, key = "", ""
    for i in range(len_key):
        crypt_by_one_symb = text[i::len_key]
        crypt_all.append(crypt_by_one_symb)
    for post in crypt_all:
        best_hi_square = min(
         ((hi_square(caesar_crypt(post, k)), k) for k in range(26)), key=lambda x: x[0]
        )[1]
        key += chr(best_hi_square + 65)
    return key

#separate text to one key's letter crypted symbols and find correct letter to shift

def improve_key(text, key):
    key = list(key)
    klen = len(key)

    improved = True
    while improved:
        improved = False

        for i in range(klen):
            stream = text[i::klen]
            current_k = ord(key[i]) - 65
            best_k = current_k
            best_score = hi_square(caesar_crypt(stream, current_k))
            for k in range(26):
                score = hi_square(caesar_crypt(stream, k))

                if score < best_score:
                    best_score = score
                    best_k = k
                    improved = True
            key[i] = chr(best_k + 65)
    return "".join(key)

#extra find hi square value in key-sized streams


def vigenere_decrypt(text, key):
    res = []
    klen = len(key)
    for indx, ch in enumerate(text):
        shift_key = ord(key[indx % klen]) - 65
        res.append(chr((ord(ch) - 65 - shift_key)%26 + 65))
    return "".join(res)

#decrypt by return correct shift back