You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_5_code import intersperse

class TestIntersperse(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_multiple_elements(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_delimeter_at_end(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_delimeter_at_start(self):
        self.assertEqual(intersperse([1, 2, 3], 0), [1, 0, 2, 0, 3])

    def test_delimeter_in_middle(self):
        self.assertEqual(intersperse([1, 2, 3], 2), [1, 2, 2, 3])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios such as empty list, single element, multiple elements, delimeter at start, delimeter at end, and delimeter in the middle.