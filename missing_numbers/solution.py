#!/usr/local/bin/python3
"""missing numbers hackerrank solution"""

import os

#
# Complete the 'missing_numbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missing_numbers(arr, brr):
    """missing numbers

    Args:
        arr (int[]): array of integers
        brr (int[]): array of integers

    Returns:
        int[]: array of missing integers
    """
    arr_obj = {}
    brr_obj = {}
    result = []

    for elem in arr:
        arr_obj[elem] = arr_obj.get(elem, 0) + 1

    for elem in brr:
        brr_obj[elem] = brr_obj.get(elem, 0) + 1

    for num, count in brr_obj.items():
        if num not in arr_obj or arr_obj[num] < count:
            result.append(num)

    return sorted(result)


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        n = int(input().strip())

        ARR = list(map(int, input().rstrip().split()))

        m = int(input().strip())

        BRR = list(map(int, input().rstrip().split()))

        RESULT = missing_numbers(ARR, BRR)

        fptr.write(' '.join(map(str, RESULT)))
        fptr.write('\n')
