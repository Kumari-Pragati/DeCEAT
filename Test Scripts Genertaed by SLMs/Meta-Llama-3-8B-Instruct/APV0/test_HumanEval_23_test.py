user

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
    return len(string)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_23_code import strlen

class TestStrlen(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)

    def test_single_character_string(self):
        self.assertEqual(strlen("a"), 1)

    def test_multiple_character_string(self):
        self.assertEqual(strlen("abc"), 3)

    def test_string_with_spaces(self):
        self.assertEqual(strlen("   "), 1)

    def test_string_with_punctuation(self):
        self.assertEqual(strlen("Hello, World!"), 13)

    def test_string_with_numbers(self):
        self.assertEqual(strlen("123"), 3)

    def test_string_with_special_characters(self):
        self.assertEqual(strlen("Hello!@#"), 12)

if __name__ == '__main__':
    unittest.main()


This script includes tests for various edge cases and common scenarios to ensure that the `strlen` function is working correctly.