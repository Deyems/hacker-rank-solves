#!/usr/local/bin/python3
"""permuting two arrays hackerrank solution
    """
import os

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#


def two_arrays(int_constant, int_arr_a, int_arr_b):
    # Write your code here
    """Checks if there exists, a permutation of two arrays where the sum of
    the elements is greater or equal to a constant k

    Args:
        int_constant (int): integer
        int_arr_a (int[]): int array
        int_arr_b (int[]): int array

    Returns:
        string: `YES` if permutation exist, 'NO' otherwise
    """
    return "NO" if any(
        a + b < int_constant for a, b in
        zip(sorted(int_arr_a),
            sorted(int_arr_b, reverse=True))) else "YES"


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        q = int(input().strip())

        for q_itr in range(q):
            first_multiple_input = input().rstrip().split()

            n = int(first_multiple_input[0])

            k = int(first_multiple_input[1])

            A = list(map(int, input().rstrip().split()))

            B = list(map(int, input().rstrip().split()))

            RESULT = two_arrays(k, A, B)

            fptr.write(RESULT + '\n')

        fptr.close()
