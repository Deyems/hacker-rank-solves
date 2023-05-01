#!/usr/local/bin/python3

import os

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    hour = s[:2]

    if s[-2:] == 'PM' and hour != '12':
        # `hour + 12 < 24` as input time is valid, Constraint
        # 01 <= hour <= 11. 12 is excluded in condition
        # `hour + 12 > 10`, therefore, will not need padding with 0
        hour = str(int(hour) + 12)
    elif s[-2:] == 'AM' and hour == '12':
        hour = '00'

    return hour + s[2:-2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
