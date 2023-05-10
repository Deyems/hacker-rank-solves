#!/usr/local/bin/python3
'''grading students hackerrank solution
'''

import os

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def grading_students(students_grades):
    # Write your code here
    """Update student grades

    Args:
        grades (int[]): students' current grades

    Returns:
        int[]: updated grades
    """
    updated_grades = []

    for grade in students_grades:
        new_grade = ((grade // 5) + 1) * \
            5 if grade > 35 and grade % 5 >= 3 else grade
        updated_grades.append(new_grade)

    return updated_grades


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w', encoding='utf-8') as fptr:

        grades_count = int(input().strip())

        grades = []

        for _ in range(grades_count):
            grades_item = int(input().strip())
            grades.append(grades_item)

        result = grading_students(grades)

        fptr.write('\n'.join(map(str, result)))
        fptr.write('\n')

        fptr.close()
