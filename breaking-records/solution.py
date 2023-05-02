#!/usr/local/bin/python3

import os

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    # Write your code here
    maxScore = float('-inf')
    minScore = float('inf')
    # adjusted for first entry
    record = [-1, -1]

    for score in scores:
        if score > maxScore:
            record[0] += 1
            maxScore = score
        if score < minScore:
            record[1] += 1
            minScore = score

    return record


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
