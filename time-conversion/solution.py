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
    sCopy = s[:-2]

    if s[-2:] == 'PM' and s[:2] != '12':
        hour = (int(sCopy[:2]) + 12) % 24
        sCopy = str(hour // 10) + str(hour % 10) + sCopy[2:]
    elif s[-2:] == 'AM' and s[:2] == '12':
        sCopy = '00' + sCopy[2:]

    return sCopy


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
