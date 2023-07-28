#!/usr/local/bin/python3
"""minimum_absolute_difference hackerrank solution"""

import os

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def minimum_absolute_difference(int_arr):
    """
    Find and return the minimum absolute difference between any two elements
    in the input list 'arr'.

    Args:
        int_arr (list): Input list of integers.

    Returns:
        int: Minimum absolute difference between any two elements in the list.

    Example:
        >>> arr = [5, 4, 3, 2, 1]
        >>> result = find_pairs_with_min_difference(arr)
        >>> print(result)
        1
    """
    sorted_arr = sorted(int_arr)
    min_diff = float('inf')

    for i in range(1, len(sorted_arr)):
        diff = sorted_arr[i] - sorted_arr[i - 1]

        if diff < min_diff:
            min_diff = diff

    return min_diff


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = minimum_absolute_difference(arr)

        fptr.write(str(result) + '\n')
