#!/usr/local/bin/python3
"""super reduced string hackerrank solution
    """
import os

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def super_reduced_string(string):
    """reduce string

    Args:
        str (string): string to be reduced

    Returns:
        string: the reduced string or 'Empty String'
    """
    pointer = 0

    while pointer < len(string) - 1:
        if string[pointer] == string[pointer + 1]:
            string = string[:pointer] + string[pointer + 2:]
            if pointer:
                pointer -= 1
        else:
            pointer += 1

    return string if string else 'Empty String'


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        s = input()

        result = super_reduced_string(s)

        fptr.write(result + '\n')

        fptr.close()
