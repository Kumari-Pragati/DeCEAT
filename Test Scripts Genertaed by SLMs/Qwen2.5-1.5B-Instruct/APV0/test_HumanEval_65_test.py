system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_65_code import circular_shift
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


assistant

import unittest

# Function to be tested
from HumanEval_65_code import circular_shift

class TestCircularShift(unittest.TestCase):

    def test_circular_shift(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(12, 2), "12")
        self.assertEqual(circular_shift(12345, 3), "451")
        self.assertEqual(circular_shift(98765, 4), "65987")
        self.assertEqual(circular_shift(10000, 5), "00001")

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a class `TestCircularShift` that inherits from `unittest.TestCase`. It contains a method `test_circular_shift` which tests the `circular_shift` function using several assertions based on the provided examples. The `if __name__ == '__main__':` block ensures that the script can be run directly or as part of a larger test suite.