system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_42_code import incr_list
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [e + 1 for e in l]


assistant

import unittest

# Importing the function to be tested
from HumanEval_42_code import incr_list

class TestIncrList(unittest.TestCase):

    def test_incr_list(self):
        # Test case 1
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

        # Test case 2
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

        # Test case 3 (empty list)
        self.assertEqual(incr_list([]), [])

        # Test case 4 (single element list)
        self.assertEqual(incr_list([7]), [8])

        # Test case 5 (list of negative numbers)
        self.assertEqual(incr_list([-1, -2, -3]), [-1, -2, -3])

        # Test case 6 (list containing both positive and negative numbers)
        self.assertEqual(incr_list([-1, 2, -3, 4, -5]), [-1, 3, -2, 5, -4])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `unittest` test case class named `TestIncrList`. It includes several test cases that cover various scenarios as described in the docstring of the `incr_list` function. The `assertEqual` method is used to verify that the output of `incr_list` matches the expected results. If any of these tests fail, the corresponding assertion will raise an error, indicating which part of the function did not behave as expected.