#!/usr/local/bin/python3
"""tower_breakers hackerrank solution"""

import os

#
# Complete the 'tower_breakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def tower_breakers(number_of_towers, height_of_towers):
    """Tower Breakers

    Args:
        number_of_towers (int): number of towers
        height_of_towers (int): height of each tower

    Returns:
        int: player who wins the game
    """
    return 1 if number_of_towers & 1 and height_of_towers > 1 else 2


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        t = int(input().strip())

        for t_itr in range(t):
            first_multiple_input = input().rstrip().split()

            n = int(first_multiple_input[0])

            m = int(first_multiple_input[1])

            RESULT = tower_breakers(n, m)

            fptr.write(str(RESULT) + '\n')
