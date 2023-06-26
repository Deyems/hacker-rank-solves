#!/usr/local/bin/python3
"""number_line_jump hackerrank solution
    """
import os

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#


def kangaroo(x_1, v_1, x_2, v_2):
    """compute if 2 kangaroos with given speed and position can be at the same
    position after a number of steps

    Args:
        x_1 (int): position 1
        v_1 (int): rate 1
        x_2 (int): position 2
        v_2 (int): rate 2

    Returns:
        string: "YES" if kangaroos can be at the same position, "NO" otherwise
    """
    if v_1 == v_2 and x_1 != x_2:
        return "NO"

    kangaroo_1 = x_1
    kangaroo_2 = x_2

    while kangaroo_1 != kangaroo_2:
        if v_1 > v_2 and kangaroo_1 > kangaroo_2:
            return "NO"
        if v_2 > v_1 and kangaroo_2 > kangaroo_1:
            return "NO"
        kangaroo_1 += v_1
        kangaroo_2 += v_2

    return "YES"


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        first_multiple_input = input().rstrip().split()

        x1 = int(first_multiple_input[0])

        v1 = int(first_multiple_input[1])

        x2 = int(first_multiple_input[2])

        v2 = int(first_multiple_input[3])

        RESULT = kangaroo(x1, v1, x2, v2)

        fptr.write(RESULT + '\n')

        fptr.close()
