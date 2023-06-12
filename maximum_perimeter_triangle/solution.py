#!/usr/local/bin/python3
"""maximum_perimeter_triangle hackerrank solution
    """
import os

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#


def maximum_perimeter_triangle(sticks_arr):
    """Given an array of stick lengths, use 3 of them to construct a
    non-degenerate triangle with the maximum possible perimeter. 

    Args:
        sticks (int[]): array of sticks

    Returns:
        int[]: array of the lengths of its sides as  integers in non-decreasing
        order
    """
    result_l = [-1]

    sticks_arr.sort()
    for i in range(len(sticks_arr) - 2):
        if sticks_arr[i] + sticks_arr[i + 1] <= sticks_arr[i + 2]:
            continue
        result_l = [sticks_arr[i], sticks_arr[i + 1], sticks_arr[i + 2]]

    return result_l


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        n = int(input().strip())

        sticks = list(map(int, input().rstrip().split()))

        result = maximum_perimeter_triangle(sticks)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

        fptr.close()
