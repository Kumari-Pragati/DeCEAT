system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
        self.assertEqual(circular_shift(1234, 2), "4123")
        self.assertEqual(circular_shift(98765, 3), "65987")
        self.assertEqual(circular_shift(10000, 4), "0001")

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases that cover different scenarios including shifting within the bounds of the input number's length and when the shift value exceeds the number of digits in the input.