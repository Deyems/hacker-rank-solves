#!/usr/local/bin/python3
'''lonely integer hackerrank solution
'''
import os

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


# def lonely_integer(arr):
#     """return the lonely, unique interger in an array

#     Args:
#         arr (int[]): integer array

#     Returns:
#         int: lonely integer
#     """
#     int_dict = {}

#     for item in arr:
#         int_dict[item] = int_dict.get(item, 0) + 1

#     for key, value in int_dict.items():
#         if value == 1:
#             return key

#     return 0

def lonely_integer(arr):
    """return the lonely, unique interger in an array

    Args:
        arr (int[]): integer array

    Returns:
        int: lonely integer
    """
    answer = 0

    for item in arr:
        answer ^= item

    return answer


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = lonely_integer(a)

        fptr.write(str(result) + '\n')

        fptr.close()
