#!/usr/local/bin/python3
"""flipping bits hackerank solution
    """

import os

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def flipping_bits(number):
    # Write your code here
    """flip bits in given number

    Args:
        number (int): number

    Returns:
        int: flipped number
    """
    return 2**32 + ~number


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        q = int(input().strip())

        for q_itr in range(q):
            n = int(input().strip())

            result = flipping_bits(n)

            fptr.write(str(result) + '\n')

        fptr.close()
