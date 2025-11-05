Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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

    def test_empty_strings(self):
        self.assertEqual(reverse_delete("", ""), ('', True))

    def test_single_character(self):
        self.assertEqual(reverse_delete("a", "a"), ('', False))
        self.assertEqual(reverse_delete("a", ""), ('a', True))

    def test_no_common_characters(self):
        self.assertEqual(reverse_delete("abcdef", "ghijkl"), ('abcdef', True))

    def test_common_characters_removed(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))

    def test_palindrome_after_deletion(self):
        self.assertEqual(reverse_delete("abccba", "bc"), ('a', True))
        self.assertEqual(reverse_delete("abccba", "ac"), ('b', False))

    def test_non_palindrome_after_deletion(self):
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))
        self.assertEqual(reverse_delete("abcdefg", "ef"), ('abcdg', False))

if __name__ == '__main__':
    unittest.main()