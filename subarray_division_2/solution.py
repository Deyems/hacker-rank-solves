#!/usr/local/bin/python3
"""subarray division hackerrank solution
    """
import os

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#


def birthday(chocolate_bar, birth_day, birth_month):
    # Write your code here
    """compute number of ways a bar of chocolate represented by an array of
    intergers using the day and month of birth.

    Args:
        s (int[]): chocolate bar
        d (int): day of birth
        m (int): month of birth

    Returns:
        int: number of ways bar can be split
    """
    i = 0
    split_count = 0

    while i < len(chocolate_bar):
        if sum(chocolate_bar[i:i+birth_month]) == birth_day:
            split_count += 1
        i += 1

    return split_count


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        RESULT = birthday(s, d, m)

        fptr.write(str(RESULT) + '\n')

        fptr.close()
