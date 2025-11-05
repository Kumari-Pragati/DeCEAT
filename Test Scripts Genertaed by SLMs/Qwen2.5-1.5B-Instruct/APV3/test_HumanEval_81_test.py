system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_81_code import unknown_function
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

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

# Importing the function we want to test
from HumanEval_81_code import unknown_function

class TestNumericalLetterGrade(unittest.TestCase):
    
    # Test case for positive numbers
    def test_positive_numbers(self):
        result = unknown_function([4.0, 3.5, 1.7])
        expected = ["A+", "A-", "C+"]
        self.assertEqual(result, expected)
        
    # Test case for negative numbers
    def test_negative_numbers(self):
        result = unknown_function([-4.0, -3.5, -1.7])
        expected = ["E", "E", "E"]
        self.assertEqual(result, expected)
        
    # Test case for empty list
    def test_empty_list(self):
        result = unknown_function([])
        expected = []
        self.assertEqual(result, expected)
        
    # Test case for mixed values
    def test_mixed_values(self):
        result = unknown_function([4.0, 3.5, -1.7, 2.0])
        expected = ["A+", "A-", "C-", "B+"]
        self.assertEqual(result, expected)
        
    # Test case for floating point numbers
    def test_floats(self):
        result = unknown_function([3.9, 3.2, 2.8])
        expected = ["A-", "B+", "C"]
        self.assertEqual(result, expected)
        
    # Test case for zero value
    def test_zero_value(self):
        result = unknown_function([0.0])
        expected = ["E"]
        self.assertEqual(result, expected)
        
    # Test case for non-numeric input
    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            unknown_function(["a", 3.5, 2.7])

if __name__ == '__main__':
    unittest.main()