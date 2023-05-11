#!/usr/local/bin/python3
"""counting valleys hackerrank solution
    """

import os

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def counting_valleys(_, path):
    # Write your code here
    """count valleys in path

    Args:
        steps (int): number of steps
        path (string): path string

    Returns:
        int: number of valleys in path
    """
    distance_from_sea_level = 0
    valley_count = 0

    for step in path:
        if step == 'U':
            distance_from_sea_level += 1
            if distance_from_sea_level == 0:
                valley_count += 1
        if step == 'D':
            distance_from_sea_level -= 1

    return valley_count


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        steps = int(input().strip())

        path = input()

        result = counting_valleys(steps, path)

        fptr.write(str(result) + '\n')

        fptr.close()
