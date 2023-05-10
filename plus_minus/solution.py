#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    zeros = 0
    positives = 0
    negatives = 0

    for elem in arr:
        if elem == 0:
            zeros += 1
        elif elem > 0:
            positives += 1
        else:
            negatives += 1

    print('{0:0.6f}'.format(positives/len(arr)))
    print('{0:0.6f}'.format(negatives/len(arr)))
    print('{0:0.6f}'.format(zeros/len(arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
