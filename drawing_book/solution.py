#!/usr/local/bin/python3
"""maximum_perimeter_triangle hackerrank solution
    """
import os

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def page_count(num_pages, page_to_turn):
    # Write your code here
    """find and print the minimum number of pages that must be turned in
    order to arrive at page page_to_turn.

    Args:
        num_pages (int): number of pages in the book
        page_to_turn (int): page number to turn to

    Returns:
        int: minimum number of pages turned
    """
    return min(page_to_turn // 2, num_pages // 2 - page_to_turn // 2)


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        n = int(input().strip())

        p = int(input().strip())

        result = page_count(n, p)

        fptr.write(str(result) + '\n')

        fptr.close()
