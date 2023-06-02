#!/usr/local/bin/python3
"""sales by match hackerrank solution
    """
import os

#
# Complete the 'sock_merchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sock_merchant(_, sock_ar):
    """match sock by color(number in array)

    Args:
        _ (int): number of elements in array
        sock_ar (int[]): color of sock in array

    Returns:
        int: number of pairs formed
    """
    sock_store = {}
    sock_pair = 0

    for sock in sock_ar:
        sock_store[sock] = not sock_store.get(sock, False)
        if not sock_store[sock]:
            sock_pair += 1

    return sock_pair


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        n = int(input().strip())

        ar = list(map(int, input().rstrip().split()))

        RESULT = sock_merchant(n, ar)

        fptr.write(str(RESULT) + '\n')

        fptr.close()
