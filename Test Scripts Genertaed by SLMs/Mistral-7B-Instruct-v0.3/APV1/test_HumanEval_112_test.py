You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_112_code import reverse_delete

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def reverse_delete(s, c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd', False)
    For s = "abcdef", c = "b"  the result should be ('acdef', False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc', True)
    """

    s = ''.join([char for char in s if char not in c])
    return (s, s[::-1] == s)

 Here is a comprehensive unittest test suite for the given Python function `reverse_delete`.


import unittest
from HumanEval_112_code import reverse_delete

class TestReverseDelete(unittest.TestCase):

    def test_reverse_delete_simple(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))
        self.assertEqual(reverse_delete("a", "a"), ('', False))
        self.assertEqual(reverse_delete("aa", "a"), ('', False))
        self.assertEqual(reverse_delete("ab", "ab"), ('', False))

    def test_reverse_delete_empty_string(self):
        self.assertEqual(reverse_delete("", "a"), ('', True))
        self.assertEqual(reverse_delete("", ""), ('', True))

    def test_reverse_delete_single_char(self):
        self.assertEqual(reverse_delete("a", "b"), ('', False))
        self.assertEqual(reverse_delete("b", "a"), ('', False))

    def test_reverse_delete_palindrome(self):
        self.assertEqual(reverse_delete("racecar", "c"), ('racer', True))
        self.assertEqual(reverse_delete("level", "l"), ('evil', True))

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as simple strings, empty strings, single characters, and palindromes. It also checks for edge cases where the input string or the characters in the input string are empty.