user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

Here is the comprehensive unittest test suite for the given Python function:


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
        self.assertEqual(intersperse([1, 2, 3, 4, 5], 4), [1, 4, 2, 4, 3, 4, 5])

    def test_list_with_negative_numbers(self):
        self.assertEqual(intersperse([-1, -2, -3], 4), [-1, 4, -2, 4, -3])

    def test_list_with_zero(self):
        self.assertEqual(intersperse([0, 1, 2], 4), [0, 4, 1, 4, 2])

    def test_list_with_large_numbers(self):
        self.assertEqual(intersperse([100, 200, 300], 4), [100, 4, 200, 4, 300])

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            intersperse([1, 'a', 3], 4)

    def test_list_with_non_integer_delimeter(self):
        with self.assertRaises(TypeError):
            intersperse([1, 2, 3], 'a')

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including:

* Empty list
* Single-element list
* Two-element list
* Three-element list
* Four-element list
* Five-element list
* List with negative numbers
* List with zero
* List with large numbers
* List with mixed types (to test for TypeError)
* List with non-integer delimeter (to test for TypeError)

Each test method checks the output of the `intersperse` function against the expected result using the `assertEqual` method. The `assertRaises` method is used to test for TypeError in cases where the input list contains non-integer elements or the delimeter is not an integer.