user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_54_code import same_chars
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return set(s0) == set(s1)assistant

Here is the unittest test script for the `same_chars` function:

import unittest
from HumanEval_54_code import same_chars

class TestSameChars(unittest.TestCase):
    def test_same_chars(self):
        # Test cases from the docstring
        self.assertTrue(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))
        self.assertTrue(same_chars('abcd', 'dddddddabc'))
        self.assertTrue(same_chars('dddddddabc', 'abcd'))
        self.assertFalse(same_chars('eabcd', 'dddddddabc'))
        self.assertFalse(same_chars('abcd', 'dddddddabce'))
        self.assertFalse(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))

        # Additional test cases
        self.assertTrue(same_chars('hello', 'olleh'))
        self.assertFalse(same_chars('hello', 'goodbye'))
        self.assertTrue(same_chars('abc', 'cab'))
        self.assertFalse(same_chars('abc', 'def'))

    def test_empty_strings(self):
        # Test empty strings
        self.assertTrue(same_chars('', ''))
        self.assertFalse(same_chars('', 'a'))
        self.assertFalse(same_chars('a', ''))

    def test_single_char_strings(self):
        # Test single-character strings
        self.assertTrue(same_chars('a', 'a'))
        self.assertFalse(same_chars('a', 'b'))
        self.assertFalse(same_chars('b', 'a'))

if __name__ == '__main__':
    unittest.main()

This script defines three test methods:

1. `test_same_chars`: Tests the `same_chars` function with a variety of input strings, including the test cases from the docstring.
2. `test_empty_strings`: Tests the `same_chars` function with empty strings.
3. `test_single_char_strings`: Tests the `same_chars` function with single-character strings.

The `unittest.main()` call at the end runs the tests.