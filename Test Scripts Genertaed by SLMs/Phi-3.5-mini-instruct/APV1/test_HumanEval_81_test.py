You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_81_code import numerical_letter_grade

class TestNumericalLetterGrade(unittest.TestCase):

    def test_numerical_letter_grade_4_0(self):
        self.assertEqual(numerical_letter_grade([4.0]), ['A+'])

    def test_numerical_letter_grade_3(self):
        self.assertEqual(numerical_letter_grade([3]), ['B'])

    def test_numerical_letter_grade_3_3(self):
        self.assertEqual(numerical_letter_grade([3.3]), ['A-'])

    def test_numerical_letter_grade_3_7(self):
        self.assertEqual(numerical_letter_grade([3.7]), ['A'])

    def test_numerical_letter_grade_2_7(self):
        self.assertEqual(numerical_letter_grade([2.7]), ['B'])

    def test_numerical_letter_grade_2_3(self):
        self.assertEqual(numerical_letter_grade([2.3]), ['B-'])

    def test_numerical_letter_grade_2_0(self):
        self.assertEqual(numerical_letter_grade([2.0]), ['C+'])

    def test_numerical_letter_grade_1_7(self):
        self.assertEqual(numerical_letter_grade([1.7]), ['C'])

    def test_numerical_letter_grade_1_3(self):
        self.assertEqual(numerical_letter_grade([1.3]), ['C-'])

    def test_numerical_letter_grade_1_0(self):
        self.assertEqual(numerical_letter_grade([1.0]), ['D+'])

    def test_numerical_letter_grade_0_7(self):
        self.assertEqual(numerical_letter_grade([0.7]), ['D'])

    def test_numerical_letter_grade_0_0(self):
        self.assertEqual(numerical_letter_grade([0.0]), ['E'])

    def test_numerical_letter_grade_multiple_grades(self):
        self.assertEqual(numerical_letter_grade([4.0, 3, 3.3, 2.7, 1.7, 1.3, 0.7, 0.0]),
                         ['A+', 'B', 'A-', 'B', 'C', 'C-', 'D', 'E'])

if __name__ == '__main__':
    unittest.main()