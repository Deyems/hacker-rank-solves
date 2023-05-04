#!/usr/local/bin/python3

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


def divisibleSumPairs(n, k, ar):
    # O (n + k)
    remainder_store = {}

    for i in range(0, k):
        remainder_store[i] = 0

    for number in ar:
        remainder_store[number % k] += 1

    # multiples combine with one another
    total_pairs = int(1/2 * remainder_store[0] * (remainder_store[0] - 1))

    # half the divisor combine with one another
    if k % 2 == 0:
        total_pairs += int(1/2 *
                           remainder_store[k/2] * (remainder_store[k/2] - 1))

    # combine other numbers
    for remainder in range(1, int((k + 1) / 2)):
        total_pairs += remainder_store[remainder] * \
            (remainder_store[k-remainder])

    return total_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
