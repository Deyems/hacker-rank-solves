#!/usr/local/bin/python3
"""dynamic_array hackerrank solution"""

import os

#
# Complete the 'dynamic_array' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamic_array(a_n, queries):
    """dynamic_array

    Args:
        a_n (int): number of arrays
        queries (str[]): queries

    Returns:
        int[]: array of query results for type 2
    """
    arr = [[] for _ in range(a_n)]
    last_answer = 0
    answers = []

    for query in queries:
        q_type, q_x, q_y = query
        idx = (q_x ^ last_answer) % n
        if q_type == 1:
            arr[idx].append(q_y)
        else:
            last_answer = arr[idx][q_y % len(arr[idx])]
            answers.append(last_answer)

    return answers


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        q = int(first_multiple_input[1])

        queries_input = []

        for _ in range(q):
            queries_input.append(list(map(int, input().rstrip().split())))

        RESULT = dynamic_array(n, queries_input)

        fptr.write('\n'.join(map(str, RESULT)))
        fptr.write('\n')
