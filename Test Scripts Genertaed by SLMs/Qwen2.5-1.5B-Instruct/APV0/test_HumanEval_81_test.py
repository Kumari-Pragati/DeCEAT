system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_81_code import unknown_function
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """

    letter_grade = []
        for gpa in grades:
            if gpa == 4.0:
                letter_grade.append("A+")
            elif gpa > 3.7:
                letter_grade.append("A")
            elif gpa > 3.3:
                letter_grade.append("A-")
            elif gpa > 3.0:
                letter_grade.append("B+")
            elif gpa > 2.7:
                letter_grade.append("B")
            elif gpa > 2.3:
                letter_grade.append("B-")
            elif gpa > 2.0:
                letter_grade.append("C+")
            elif gpa > 1.7:
                letter_grade.append("C")
            elif gpa > 1.3:
                letter_grade.append("C-")
            elif gpa > 1.0:
                letter_grade.append("D+")
            elif gpa > 0.7:
                letter_grade.append("D")
            elif gpa > 0.0:
                letter_grade.append("D-")
            else:
                letter_grade.append("E")
        return letter_grade


assistant

import unittest

# Assuming the existence of the function `numerical_letter_grade`
from HumanEval_81_code import numerical_letter_grade

class TestNumericalLetterGrade(unittest.TestCase):

    def test_grades(self):
        # Test case 1: All grades above 4.0
        self.assertEqual(numerical_letter_grade([4.0, 4.0, 4.0]), ["A+", "A+", "A+"], "Test Case 1 Failed")

        # Test case 2: Grades between 3.7 and 4.0
        self.assertEqual(numerical_letter_grade([3.9, 3.8, 4.1]), ["A-", "A-", "A+"])

        # Test case 3: Grades below 0.0
        self.assertEqual(numerical_letter_grade([-0.1, -0.5, 0.0]), ["E", "E", "E"])

        # Test case 4: Mixed grades (including negative)
        self.assertEqual(numerical_letter_grade([4.5, -2.0, 3.2, 1.9]), ["A+", "E", "B+", "D-"])

        # Test case 5: Empty input
        self.assertEqual(numerical_letter_grade([]), [], "Test Case 5 Failed")

if __name__ == '__main__':
    unittest.main()


This script defines a unit test class `TestNumericalLetterGrade` which inherits from `unittest.TestCase`. It contains several test cases to ensure the `numerical_letter_grade` function works as expected across different scenarios. The `assertEqual` method is used to compare the actual result of the function with the expected outcome. If any test fails, it will raise an assertion error, indicating where the failure occurred.