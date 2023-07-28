#!/usr/local/bin/python3
"""caesar_cipher hackerrank solution"""

import os

#
# Complete the 'caesar_cipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesar_cipher(string, shift_k):
    """Caesar Cipher

    Args:
        string (str): string to encrypt
        shift_k (int): number of letters to rotate

    Returns:
        str: encrypted string
    """
    encrypted_string = ''

    for letter in string:
        if letter.isalpha():
            if letter.isupper():
                encrypted_string += chr(((ord(letter) -
                                        65 + shift_k) % 26) + 65)
            else:
                encrypted_string += chr(((ord(letter) -
                                        97 + shift_k) % 26) + 97)
        else:
            encrypted_string += letter

    return encrypted_string


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        n = int(input().strip())

        s = input()

        k = int(input().strip())

        result = caesar_cipher(s, k)

        fptr.write(result + '\n')
