#!/usr/local/bin/python3
"""counting sort 1 hackerrank solution
    """

import os

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def counting_sort(int_arr):
    # Write your code here
    """Implements counting sort on integer array

    Args:
        int_arr (int[]): integer array

    Returns:
        int[]: number-indexed frequency array
    """
    count_array = [0] * 100

    for number in int_arr:
        count_array[number] += 1

    return count_array


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = counting_sort(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

        fptr.close()
