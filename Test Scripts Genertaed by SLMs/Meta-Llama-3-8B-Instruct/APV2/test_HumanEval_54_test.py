system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the `same_chars` function:


import unittest
from HumanEval_54_code import same_chars

class TestSameChars(unittest.TestCase):

    def test_same_chars_true(self):
        self.assertTrue(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))
        self.assertTrue(same_chars('abcd', 'dddddddabc'))
        self.assertTrue(same_chars('dddddddabc', 'abcd'))
        self.assertTrue(same_chars('eabcd', 'eabcd'))
        self.assertTrue(same_chars('abcd', 'abcd'))

    def test_same_chars_false(self):
        self.assertFalse(same_chars('eabcd', 'dddddddabc'))
        self.assertFalse(same_chars('abcd', 'dddddddabce'))
        self.assertFalse(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))
        self.assertFalse(same_chars('eabcd', 'eabcdz'))
        self.assertFalse(same_chars('abcd', 'abcdz'))

    def test_same_chars_edge_cases(self):
        self.assertTrue(same_chars('', ''))
        self.assertFalse(same_chars('a', ''))
        self.assertFalse(same_chars('', 'a'))
        self.assertTrue(same_chars('a', 'a'))

if __name__ == '__main__':
    unittest.main()