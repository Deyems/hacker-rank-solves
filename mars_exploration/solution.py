#!/usr/local/bin/python3
"""mars exploration hackerrank solution
    """

import os

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def mars_exploration(message):
    """Compute deviation in distress message from MARS rover

    Args:
        message (string): distress message

    Returns:
        int: number of characters changed
    """
    deviation = 0

    for i, character in enumerate(message):
        if i % 3 != 1 and character != 'S':
            deviation += 1
        if i % 3 == 1 and character != 'O':
            deviation += 1

    return deviation


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        s = input()

        result = mars_exploration(s)

        fptr.write(str(result) + '\n')

        fptr.close()
