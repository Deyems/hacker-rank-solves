#!/usr/local/bin/python3
"""rotate_left hackerrank solution
    """
import os

#
# Complete the 'rotate_left' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#


def rotate_left(rotate_num, int_arr):
    """shift every of the array's elements `rotate_num` units to the left

    Args:
        rotate_num (int): amount to rotate by
        int_arr (int[]): the array to rotate

    Returns:
        int[]: the rotated array
    """
    return int_arr[rotate_num:] + int_arr[:rotate_num]


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        d = int(first_multiple_input[1])

        arr = list(map(int, input().rstrip().split()))

        result = rotate_left(d, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

        fptr.close()
