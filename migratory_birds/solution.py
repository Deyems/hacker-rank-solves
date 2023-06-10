#!/usr/local/bin/python3
"""migratory birds hackerrank solution
    """
import os

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratory_birds(birds_sighted):
    """migratory birds

    Args:
        arr (int[]): birds sighted

    Returns:
        int: lowest type id of the most frequently sighted birds
    """
    max_freq = 0
    max_occuring_bird_with_smallest_id = birds_sighted[0]

    for unique_bird in set(birds_sighted):
        freq = birds_sighted.count(unique_bird)
        if freq > max_freq:
            max_freq = freq
            max_occuring_bird_with_smallest_id = unique_bird
        elif freq == max_freq and unique_bird < max_occuring_bird_with_smallest_id:
            max_occuring_bird_with_smallest_id = unique_bird

    return max_occuring_bird_with_smallest_id


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = migratory_birds(arr)

        fptr.write(str(result) + '\n')

        fptr.close()
