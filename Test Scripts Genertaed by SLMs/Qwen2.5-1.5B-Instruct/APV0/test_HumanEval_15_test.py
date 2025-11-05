system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

# Importing the function from the provided code snippet
from HumanEval_15_code import string_sequence

class TestStringSequence(unittest.TestCase):
    def test_string_sequence(self):
        # Test cases for different values of n
        self.assertEqual(string_sequence(0), "0")
        self.assertEqual(string_sequence(5), "0 1 2 3 4 5")
        self.assertEqual(string_sequence(10), "0 1 2 3 4 5 6 7 8 9 10")

    def test_negative_input(self):
        # Testing with negative input (should raise an error)
        with self.assertRaises(ValueError):
            string_sequence(-1)

    def test_non_integer_input(self):
        # Testing with non-integer input (should raise a TypeError)
        with self.assertRaises(TypeError):
            string_sequence("abc")

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and `string_sequence`, then defines a class `TestStringSequence` that inherits from `unittest.TestCase`. It includes methods to test the `string_sequence` function with various inputs, including edge cases like negative integers and non-integer inputs. The `assertEqual` method is used to check if the output matches the expected results, and the `with self.assertRaises(...)` statements ensure that exceptions are raised when invalid inputs are passed to the function. Finally, the `unittest.main()` call runs all tests defined in the class.