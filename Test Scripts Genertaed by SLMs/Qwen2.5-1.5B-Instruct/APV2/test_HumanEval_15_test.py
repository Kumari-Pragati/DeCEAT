system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

# Provided function
from HumanEval_15_code import string_sequence

class TestStringSequence(unittest.TestCase):
    
    def test_string_sequence(self):
        # Test cases for different values of n
        self.assertEqual(string_sequence(0), "0")
        self.assertEqual(string_sequence(5), "0 1 2 3 4 5")
        self.assertEqual(string_sequence(10), "0 1 2 3 4 5 6 7 8 9 10")

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases covering various inputs (n=0, n=5, n=10). It uses `assertEqual` to check if the output matches the expected results. If any of these tests fail, it will raise an assertion error indicating which test failed and what the expected result was.