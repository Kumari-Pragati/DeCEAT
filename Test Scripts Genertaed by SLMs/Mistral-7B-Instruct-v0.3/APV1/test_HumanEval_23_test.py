You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a simple unittest test suite for the `strlen` function. I've included a few test cases to cover the edge cases and basic functionality.


import unittest
from HumanEval_23_code import strlen

class TestStrlen(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_single_character_string(self):
        self.assertEqual(strlen('a'), 1)
        self.assertEqual(strlen('z'), 1)

    def test_multi_character_string(self):
        self.assertEqual(strlen('abc'), 3)
        self.assertEqual(strlen('123'), 3)
        self.assertEqual(strlen('ABC'), 3)

    def test_string_with_spaces(self):
        self.assertEqual(strlen('hello world'), 11)
        self.assertEqual(strlen('  spaces   '), 6)

    def test_string_with_special_characters(self):
        self.assertEqual(strlen('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 47)
        self.assertEqual(strlen('abc!123'), 7)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty string, single-character strings, multi-character strings, strings with spaces, and strings with special characters. It uses the `assertEqual` method to check if the output of the `strlen` function matches the expected output for each test case.