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

 import unittest
from HumanEval_112_code import reverse_delete

class TestReverseDelete(unittest.TestCase):

    def test_reverse_delete_empty_strings(self):
        self.assertEqual(reverse_delete("", ""), ('', True))

    def test_reverse_delete_no_match(self):
        self.assertEqual(reverse_delete("abcde", "xy"), ('abcde', False))

    def test_reverse_delete_all_chars_removed(self):
        self.assertEqual(reverse_delete("abcdef", "abc"), ('', False))

    def test_reverse_delete_palindrome_result(self):
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))

    def test_reverse_delete_non_palindrome_result(self):
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))

    def test_reverse_delete_single_char_removed(self):
        self.assertEqual(reverse_delete("abcde", "a"), ('bcde', False))

    def test_reverse_delete_multiple_chars_removed(self):
        self.assertEqual(reverse_delete("abcde", "cd"), ('a', False))

    def test_reverse_delete_case_insensitive(self):
        self.assertEqual(reverse_delete("AbCde", "a"), ('BCd', False))

    def test_reverse_delete_empty_string_case_insensitive(self):
        self.assertEqual(reverse_delete("", "A"), ('', True))

if __name__ == '__main__':
    unittest.main()