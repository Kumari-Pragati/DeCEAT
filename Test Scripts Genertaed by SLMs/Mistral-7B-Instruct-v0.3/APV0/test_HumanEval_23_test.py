Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_23_code import strlen
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

 Here is a simple unittest test script for the `strlen` function. The test cases cover the base case (empty string), a single character string, and a multi-character string.


import unittest
from HumanEval_23_code import strlen

class TestStrlenFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_single_character_string(self):
        self.assertEqual(strlen('a'), 1)
        self.assertEqual(strlen('z'), 1)

    def test_multi_character_string(self):
        self.assertEqual(strlen('abc'), 3)
        self.assertEqual(strlen('xyz'), 3)
        self.assertEqual(strlen('123'), 3)
        self.assertEqual(strlen('!@#'), 3)

if __name__ == '__main__':
    unittest.main()


This script can be run directly using the command `python test_strlen.py` from the terminal or command prompt.