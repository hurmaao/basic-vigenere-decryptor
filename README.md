# Vigenere Cipher Decryptor

A Python tool for automatically decrypting text encrypted with the Vigenère cipher.

## Overview

This project implements cryptoanalysis system for breaking the Vigenere cipher using:
- **Kasiski examination** to determine key lenght
- **Frequency analysis** to find probable key characters
- **Chi-squared statictic** to measure similarity to english text
- **Iterative key improvement** for better results

## Usage

-  Run the program:
    ```bash
     python main.py
-  Paste your encrypted text and press Ctrl+D (Linux/Mac) or Ctrl+Z then Enter (Windows) to finish
-  The program will:
     Display probable key length
     Suggest decryption key
     Allow manual key verification
> The program may have errors depending on the length of the key and text
     Output decrypted text
