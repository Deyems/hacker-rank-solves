#!/usr/local/bin/python3
"""picking numbers hackerrank solution
    """
import os

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def picking_numbers(int_arr):
    """Given an array of integers, find the longest subarray where the absolute
    difference between any two elements is less than or equal to 1.

    Args:
        int_arr (int[]): array of integers

    Returns:
        int: the length of the longest subarray that meets the criterion
    """

    # get number counts (can use Counter from collections)
    number_store = {}
    for num in int_arr:
        if num in number_store:
            number_store[num] += 1
        else:
            number_store[num] = 1
    vals = sorted(number_store.keys())

    # current value
    current_value = vals[0]
    max_subarray_length = number_store[vals[0]]

    # test the entire list of adjacent keys
    for num in vals[1:]:

        # result may be based on only 1 element count
        max_subarray_length = max(max_subarray_length, number_store[num])

        # check situation with 2 elements
        if num - current_value == 1:
            max_subarray_length = max(
                max_subarray_length, number_store[num]+number_store[current_value])

        current_value = num
    return max_subarray_length


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = picking_numbers(a)

        fptr.write(str(result) + '\n')

        fptr.close()
