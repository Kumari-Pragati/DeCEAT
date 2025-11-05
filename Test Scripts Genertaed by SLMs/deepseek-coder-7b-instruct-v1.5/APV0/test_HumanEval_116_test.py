You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_116_code import sort_array
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_116_code import sort_array

class TestSortArray(unittest.TestCase):
    def test_sort_array(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])
        self.assertEqual(sort_array([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
        self.assertEqual(sort_array([10, 20, 30, 40, 50]), [10, 20, 30, 40, 50])
        self.assertEqual(sort_array([100, 200, 300, 400, 500]), [100, 200, 300, 400, 500])
        self.assertEqual(sort_array([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()


This script tests the `sort_array` function with a variety of inputs to ensure it's working correctly. The `assertEqual` method is used to check that the output of the function matches the expected output for each test case.

Please note that the `HumanEval_116_code` module should contain the `sort_array` function for these tests to work. If the function is not in a separate module, you can replace `from HumanEval_116_code import sort_array` with `sort_array = sort_array`.