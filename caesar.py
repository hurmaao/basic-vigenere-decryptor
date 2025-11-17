def caesar_crypt(text, shift):
    return "".join(chr((ord(c) - 65 - shift) % 26 + 65) for c in text)

#decrypt by caesar