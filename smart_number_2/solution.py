#!/usr/local/bin/python3
"""is_smart_number"""
import math


def is_smart_number(num):
    """Is smart number if number has an odd number of factors.

    Args:
        num (int): Number to check.

    Returns:
        bool: if number is a smart number.
    """
    val = int(math.sqrt(num))
    if num / val == val:
        return True
    return False


for _ in range(int(input())):
    NUM = int(input())
    ANS = is_smart_number(NUM)
    if ANS:
        print("YES")
    else:
        print("NO")
