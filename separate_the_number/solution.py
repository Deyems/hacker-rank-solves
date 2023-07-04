#!/usr/local/bin/python3
"""separate_numbers hackerrank solution"""

#
# Complete the 'separate_numbers' function below.
#
# The function accepts STRING s as parameter.
#


def separate_numbers(string_to_check):
    """Prints whether or not the string is beautiful on a new line.

    Args:
        string_to_check (string): string to check
    """
    if len(string_to_check) == 1 or string_to_check[0] == '0':
        print('NO')
        return

    for i in range(1, (int)(len(string_to_check)/2)+1):
        start = string_to_check[:i]
        val = int(start)
        compare = ""

        while len(compare) < len(string_to_check[i:]):
            val = val + 1
            compare = compare + str(val)

        if compare == string_to_check[i:]:
            print(f'YES {int(start)}')
            return

    print('NO')


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separate_numbers(s)
