You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_5_code import intersperse
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result: List[int] = []
    for i, x in enumerate(numbers):
        result.append(x)
        if i != len(numbers) - 1:
            result.append(delimeter)
    return result

 Here is the complete unittest test suite for the `intersperse` function:


import unittest
from HumanEval_5_code import intersperse

class TestIntersparse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_two_elements_list(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_multiple_elements_list(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_negative_elements_list(self):
        self.assertEqual(intersperse([-1, -2, -3], 4), [-1, 4, -2, 4, -3])

    def test_mixed_elements_list(self):
        self.assertEqual(intersperse([1, -2, 3, -4], 4), [1, 4, -2, 4, 3, 4, -4])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases for different scenarios, such as an empty list, a single-element list, multiple elements, negative elements, and mixed elements. The test suite uses the `assertEqual` method to compare the expected output with the actual output of the `intersperse` function.