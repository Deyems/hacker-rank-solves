#!/usr/local/bin/python3
"""minimum_number hackerrank solution"""

import os

#
# Complete the 'minimum_number' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER password_length
#  2. STRING password
#


def minimum_number(password_length, password):
    """minimum_number

    Args:
        password_length (int): length of password
        password (str): password to evaluate

    Returns:
        int: minimum number of characters to add to make password strong
    """
    # The time complexity of this solution is O(n) where n is the length of the password
    # The space complexity of this solution is O(1) because the bit map is a constant size

    # 1st bit: lowercase letter
    # 2nd bit: uppercase letter
    # 3rd bit: digit
    # 4th bit: special character
    has_lower = 1
    has_upper = 1 << 1
    has_digit = 1 << 2
    has_special = 1 << 3
    all_met = has_lower | has_upper | has_digit | has_special
    # use bit map to track met conditions
    met_conditions = 0

    min_length = 6  # Minimum length of password

    # Loop through password and set bits in bit map when conditions are met
    for char in password:
        # Check if character is lowercase letter
        if char.islower():
            met_conditions |= has_lower
        # Check if character is uppercase letter
        elif char.isupper():
            met_conditions |= has_upper
        # Check if character is digit
        elif char.isdigit():
            met_conditions |= has_digit
        # Check if character is special character
        elif char in "!@#$%^&*()-+":
            met_conditions |= has_special

        # Check if all conditions are met
        if met_conditions == all_met:
            return max(0, min_length - password_length)

    # Get missing conditions
    missing_conditions = bin(all_met).count(
        '1') - bin(met_conditions).count('1')

    return max(missing_conditions, min_length - password_length)


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        n = int(input().strip())

        password_input = input()

        result = minimum_number(n, password_input)

        fptr.write(str(result) + '\n')
