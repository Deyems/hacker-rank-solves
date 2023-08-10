#!/usr/local/bin/python3
"""max_min hackerrank solution"""

import os

#
# Complete the 'max_min' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k_num
#  2. INTEGER_ARRAY int_arr
#


def max_min(k_num, int_arr):
    """Max Min

    Args:
        k_num (int): number of elements to group
        int_arr (list): array of integers

    Returns:
        int: maximum difference between k elements
    """
    sorted_arr = sorted(int_arr)
    return min(sorted_arr[i + k_num - 1] - num for i, num in enumerate(sorted_arr[:-(k_num - 1)]))


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        n = int(input().strip())

        k = int(input().strip())

        arr = []

        for _ in range(n):
            arr_item = int(input().strip())
            arr.append(arr_item)

        result = max_min(k, arr)

        fptr.write(str(result) + '\n')
