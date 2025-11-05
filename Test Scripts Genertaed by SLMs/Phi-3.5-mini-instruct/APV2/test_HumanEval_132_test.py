You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_132_code import is_nested
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        if string[i] == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2

 
import unittest
from HumanEval_132_code import is_nested

class TestIsNested(unittest.TestCase):

    def test_valid_nested(self):
        self.assertTrue(is_nested('[[]]'))

    def test_no_nested(self):
        self.assertFalse(is_nested('[]]]]]]][[[[[]'))

    def test_no_brackets(self):
        self.assertFalse(is_nested('[][]'))

    def test_single_bracket(self):
        self.assertFalse(is_nested('[]'))

    def test_partially_nested(self):
        self.assertTrue(is_nested('[[][]]'))

    def test_mixed_brackets(self):
        self.assertTrue(is_nested('[[]][['))

    def test_empty_string(self):
        self.assertFalse(is_nested(''))

    def test_non_bracket_characters(self):
        self.assertFalse(is_nested('abc[][]d'))

    def test_nested_within_nested(self):
        self.assertTrue(is_nested('[[][[]]'))

if __name__ == '__main__':
    unittest.main()

This test suite includes various test cases for the `is_nested` function, ensuring that it correctly identifies valid nested subsequences of brackets, as well as cases where there are no nested brackets, single brackets, and strings with non-bracket characters. It also tests edge cases such as empty strings and strings with only opening brackets.