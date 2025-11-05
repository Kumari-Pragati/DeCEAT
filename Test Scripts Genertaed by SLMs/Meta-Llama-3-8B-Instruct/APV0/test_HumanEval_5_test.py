user

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
        if i!= len(numbers) - 1:
            result.append(delimeter)
    return resultassistant

Here is a unittest test script for the given Python function:

Python
import unittest
from HumanEval_5_code import intersperse

class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_two_element_list(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_three_element_list(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_four_element_list(self):
        self.assertEqual(intersperse([1, 2, 3, 4], 4), [1, 4, 2, 4, 3, 4])

    def test_five_element_list(self):
        self.assertEqual(intersperse([1, 2, 3, 4, 5], 4), [1, 4, 2, 4, 3, 4, 4, 5])

    def test_large_list(self):
        self.assertEqual(intersperse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4), 
                         [1, 4, 2, 4, 3, 4, 4, 5, 4, 6, 4, 7, 4, 8, 4, 9, 4, 10])

if __name__ == '__main__':
    unittest.main()


This script includes 6 test cases to cover different scenarios. The test cases cover the following scenarios:

- An empty list
- A list with a single element
- A list with two elements
- A list with three elements
- A list with four elements
- A list with five elements

Each test case checks if the output of the `intersperse` function matches the expected output.