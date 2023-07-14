#!/usr/local/bin/python3
"""closest_numbers hackerrank solution"""

import os

#
# Complete the 'separate_numbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def closest_numbers(int_arr):
    """
    Find and return a sorted list containing all pairs from the input list 'arr'
    that have the minimum absolute difference between them.

    Args:
        int_arr (list): Input list of integers.

    Returns:
        list: Sorted list containing the pairs with the minimum difference.

    Example:
        >>> arr = [5, 4, 3, 2, 1]
        >>> result = find_pairs_with_min_difference(arr)
        >>> print(result)
        [1, 2, 2, 3, 3, 4, 4, 5]
    """
    sorted_arr = sorted(int_arr)
    min_diff = float('inf')
    min_pairs = []

    for i in range(1, len(sorted_arr)):
        diff = sorted_arr[i] - sorted_arr[i - 1]

        if diff < min_diff:
            min_diff = diff
            min_pairs = [(sorted_arr[i - 1], sorted_arr[i])]
        elif diff == min_diff:
            min_pairs.append((sorted_arr[i - 1], sorted_arr[i]))

    return [elem for pair in min_pairs for elem in pair]


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = closest_numbers(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
