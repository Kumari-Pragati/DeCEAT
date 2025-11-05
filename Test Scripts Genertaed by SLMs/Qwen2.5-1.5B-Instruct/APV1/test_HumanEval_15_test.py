system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_15_code import string_sequence
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join(str(x) for x in range(n + 1))


assistant

import unittest

# Importing the function we want to test
from HumanEval_15_code import string_sequence

class TestStringSequence(unittest.TestCase):
    def test_string_sequence(self):
        # Test cases for different values of n
        self.assertEqual(string_sequence(0), "0")
        self.assertEqual(string_sequence(5), "0 1 2 3 4 5")
        self.assertEqual(string_sequence(10), "0 1 2 3 4 5 6 7 8 9 10")

    def test_negative_input(self):
        # Testing with negative input should raise ValueError
        with self.assertRaises(ValueError):
            string_sequence(-1)

    def test_non_integer_input(self):
        # Testing with non-integer input should raise TypeError
        with self.assertRaises(TypeError):
            string_sequence("abc")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `unittest` test case class named `TestStringSequence`. It includes three test methods:

1. `test_string_sequence`: This method tests the `string_sequence` function with positive integer inputs and checks if it returns the expected output strings.
2. `test_negative_input`: This method tests the function with a negative input value to ensure that it raises a `ValueError`.
3. `test_non_integer_input`: This method tests the function with a non-integer input value to ensure that it raises a `TypeError`.

The `unittest.main()` call at the end runs all the defined test methods when the script is executed directly.