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
    return''.join(str(x) for x in range(n + 1))assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_15_code import string_sequence

class TestStringSequence(unittest.TestCase):

    def test_string_sequence(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')
        self.assertEqual(string_sequence(-1), '')
        self.assertEqual(string_sequence(10), '0 1 2 3 4 5 6 7 8 9 10')
        self.assertEqual(string_sequence(1), '0')
        self.assertEqual(string_sequence(2), '0 1')
        self.assertEqual(string_sequence(3), '0 1 2')
        self.assertEqual(string_sequence(4), '0 1 2 3')
        self.assertEqual(string_sequence(6), '0 1 2 3 4 5')

if __name__ == '__main__':
    unittest.main()


This script tests the function with different inputs and checks if the output matches the expected output. The test cases include testing with a negative number, testing with a small number, and testing with a larger number.