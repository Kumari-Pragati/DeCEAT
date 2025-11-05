You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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

 
import unittest
from HumanEval_112_code import reverse_delete

class TestReverseDelete(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_delete("", "ae"), ('', False))

    def test_single_character(self):
        self.assertEqual(reverse_delete("a", "a"), ('', False))

    def test_no_match(self):
        self.assertEqual(reverse_delete("abcde", "xy"), ('abcde', False))

    def test_palindrome_result(self):
        self.assertEqual(reverse_delete("abccba", "c"), ('abba', True))

    def test_non_palindrome_result(self):
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))

    def test_empty_result(self):
        self.assertEqual(reverse_delete("", ""), ('', True))

    def test_single_character_removal(self):
        self.assertEqual(reverse_delete("abc", "a"), ('bc', False))

    def test_multiple_character_removal(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))

    def test_palindrome_after_removal(self):
        self.assertEqual(reverse_delete("abccba", "c"), ('abba', True))

    def test_non_palindrome_after_removal(self):
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))

    def test_palindrome_with_no_removal(self):
        self.assertEqual(reverse_delete("abccba", ""), ('abccba', True))

    def test_non_palindrome_with_no_removal(self):
        self.assertEqual(reverse_delete("abcdef", ""), ('abcdef', False))

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases for the `reverse_delete` function, including empty strings, single characters, no match, palindrome results, non-palindrome results, and cases where no characters are removed. It ensures that the function behaves as expected across a range of inputs.