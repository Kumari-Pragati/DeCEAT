Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `intersperse` function:


import unittest
from HumanEval_5_code import intersperse

class TestIntersparse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_simple_list(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_list_with_duplicates(self):
        self.assertEqual(intersperse([1, 2, 1, 2, 3], 4), [1, 4, 2, 4, 1, 4, 2, 4, 3])

    def test_list_with_negative_numbers(self):
        self.assertEqual(intersperse([-1, 0, 1], 4), [-1, 4, 0, 4, 1])

    def test_list_with_long_elements(self):
        self.assertEqual(intersperse([[1], [2], [3]], 4), [[1], [4], [2], [4], [3]])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases for different scenarios, such as an empty list, a single-element list, a list with duplicates, a list with negative numbers, and a list with longer elements. It uses the `assertEqual` method to verify that the expected output matches the actual output of the `intersperse` function.