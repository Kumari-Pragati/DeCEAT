You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return set(s0) == set(s1)

 Here is a comprehensive unittest test suite for the given Python function `same_chars`.


import unittest
from HumanEval_54_code import same_chars

class TestSameChars(unittest.TestCase):

    def test_same_chars_equal_strings(self):
        self.assertTrue(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))
        self.assertTrue(same_chars('abcd', 'dddddddabc'))
        self.assertTrue(same_chars('dddddddabc', 'abcd'))

    def test_same_chars_different_order(self):
        self.assertTrue(same_chars('eabcd', 'dddzzzzzzzddeddabc'))
        self.assertTrue(same_chars('abcd', 'dddddddabce'))

    def test_same_chars_different_strings(self):
        self.assertFalse(same_chars('eabcd', 'dddddddabc'))
        self.assertFalse(same_chars('abcd', 'dddddddabce'))
        self.assertFalse(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_same_chars_equal_strings` checks that the function correctly identifies when two strings have the same characters, regardless of their order.
2. `test_same_chars_different_order` checks that the function correctly identifies when two strings have the same characters, even if they are in a different order.
3. `test_same_chars_different_strings` checks that the function correctly identifies when two strings do not have the same characters.

Each test case includes multiple test cases to ensure comprehensive coverage of the function's behavior.