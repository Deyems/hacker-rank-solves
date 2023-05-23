#!/usr/local/bin/python3
"""xor strings hackerrank solution
    """


def strings_xor(binary_s, binary_t):
    """computed xor of 2 strings
    strings represent binary numbers

    Args:
        binary_s (string): binary string
        binary_t (string): binary string

    Returns:
        string: xor of 2 binary string
    """
    res = ""
    for i, _ in enumerate(binary_s):
        if binary_s[i] == binary_t[i]:
            res += '0'
        else:
            res += '1'

    return res


s = input()
t = input()
print(strings_xor(s, t))
