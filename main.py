import sys
from clean_text import clean_text
from kasiski_len_key import kasiski
from vigenere import find_key, improve_key, vigenere_decrypt


def main():
    print("Enter Crypted Text:")
    cipher = clean_text(sys.stdin.read())
    key_len = kasiski(cipher)
    print("Probable Key Lenght =", key_len)
    key = find_key(cipher, key_len)
    key2 = improve_key(cipher, key)
    print("Supposed Key =", key2)
    print("Enter Verified Key:")
    key3 = input().strip()
    plain = vigenere_decrypt(cipher, key3)
    print("Decrypted Text:")
    print(plain)

#enter text and verify key if result key have mistakes 
main()
