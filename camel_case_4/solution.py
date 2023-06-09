#!/usr/local/bin/python3
from sys import stdin


def combine(name, t):
    firstLetter = 1
    spaceFound = 0
    result = ''

    for letter in name:
        if letter.isspace():
            spaceFound = 1
            continue
        if spaceFound:
            result += letter.upper()
            spaceFound = 0
            continue
        if firstLetter and t == 'C':
            result += letter.upper()
            firstLetter = 0
            continue
        result += letter

    if t == 'M':
        result += '()'

    return result


def split(name):
    firstLetter = 1
    result = ''

    for letter in name:
        if not letter.isalpha():
            continue
        if letter.isupper() and firstLetter != 1:
            result += ' '
        firstLetter = 0
        result += letter.lower()

    return result


def camelCase(s):
    operation = s[0]

    if operation == 'C':
        print(combine(s[4:], s[2]))

    elif operation == 'S':
        print(split(s[4:]))


if __name__ == '__main__':
    for s in stdin:
        camelCase(s)
