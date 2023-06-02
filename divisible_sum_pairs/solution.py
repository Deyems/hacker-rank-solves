#!/usr/local/bin/python3
"""hackerrank divisible sum pairs solution
    """

import os

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

# O (n^2)
# def divisibleSumPairs(n, k, ar):
#     # Write your code here
#     result = 0

#     for i in range(n):
#         for j in range(i + 1, n):
#             if (ar[i] + ar[j]) % k == 0:
#                 result += 1
#     return result


def divisible_sum_pairs(_, divisor, int_ar):
    """divisible sum pairs

    Args:
        _ (int): number of elements in array; not used
        divisor (int): number to divide sum pair by
        int_ar (int[]): array of integers

    Returns:
        int: number of divisible sum pairs
    """
    # O (n + k)
    remainder_store = {}

    for number in int_ar:
        remainder_store[number % divisor] = remainder_store.get(
            number % divisor, 0) + 1

    # multiples combine with one another
    total_pairs = int(1/2 * remainder_store.get(0, 0)
                      * (remainder_store.get(0, 0) - 1))

    # half the divisor combine with one another
    if divisor % 2 == 0:
        total_pairs += int(1/2 *
                           remainder_store.get(divisor/2, 0) * (remainder_store.get(divisor/2, 0) - 1))

    # combine other numbers
    for remainder in range(1, int((divisor + 1) / 2)):
        total_pairs += remainder_store.get(remainder, 0) * \
            (remainder_store.get(divisor-remainder, 0))

    return total_pairs


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        ar = list(map(int, input().rstrip().split()))

        result = divisible_sum_pairs(n, k, ar)

        fptr.write(str(result) + '\n')

        fptr.close()
