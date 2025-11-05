You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_15_code import string_sequence

class TestStringSequence(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(string_sequence(0), '0')

    def test_positive_numbers(self):
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')
        self.assertEqual(string_sequence(10), '0 1 2 3 4 5 6 7 8 9 10')

    def test_negative_numbers(self):
        self.assertEqual(string_sequence(-5), '0 -1 -2 -3 -4 -5')
        self.assertEqual(string_sequence(-10), '0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10')

    def test_large_numbers(self):
        self.assertEqual(string_sequence(1000), ' '.join(str(x) for x in range(1001)))

if __name__ == '__main__':
    unittest.main()


This suite includes tests for zero, positive numbers, negative numbers, and large numbers. It checks if the function returns the correct output for each of these cases.

Note: This test suite assumes that the `string_sequence` function in the `HumanEval_15_code` module behaves as expected. If the function behaves differently, the test suite might need to be adjusted accordingly.