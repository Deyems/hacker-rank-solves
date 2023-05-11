#!/usr/local/bin/python3
"""diagonal difference hackerrank solution
    """
import os

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonal_difference(square_matrix):
    # Write your code here
    """compute the diagonal difference of a square matrix

    Args:
        arr (int[][]): square matrix

    Returns:
        int: difference of diagonals
    """
    return abs(sum(row[i] - row[len(square_matrix) - i - 1] for i, row in
                   enumerate(square_matrix)))


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        n = int(input().strip())

        arr = []

        for _ in range(n):
            arr.append(list(map(int, input().rstrip().split())))

        result = diagonal_difference(arr)

        fptr.write(str(result) + '\n')

        fptr.close()
