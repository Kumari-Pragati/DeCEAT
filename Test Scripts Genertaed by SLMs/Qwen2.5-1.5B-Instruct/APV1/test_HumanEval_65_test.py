system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

# Importing the function from the provided code snippet
from HumanEval_65_code import circular_shift

class TestCircularShift(unittest.TestCase):

    def test_circular_shift(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(12, 2), "12")
        self.assertEqual(circular_shift(12345, 3), "4512")
        self.assertEqual(circular_shift(9876543210, 10), "9876543210")
        self.assertEqual(circular_shift(9876543210, 11), "9876543210")
        self.assertEqual(circular_shift(9876543210, 12), "9876543210")

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure that the `circular_shift` function behaves correctly under various conditions, including when the shift value exceeds the length of the input number and when it does not.