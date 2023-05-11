#!/usr/local/bin/python3
"""pangrams hackerrank solution
    """

import os
from string import ascii_lowercase as letters

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(sentence):
    # Write your code here
    """check if string is pangram

    Args:
        sentence (str): string

    Returns:
        str: `pangram` if string is pangram `not pangram` otherwise
    """
    for letter in letters:
        if letter not in sentence.lower():
            return 'not pangram'
    return 'pangram'


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        s = input()

        result = pangrams(s)

        fptr.write(result + '\n')

        fptr.close()
