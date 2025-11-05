user

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
    return (s, s[::-1] == s)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_112_code import reverse_delete

class TestReverseDelete(unittest.TestCase):

    def test_reverse_delete(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))
        self.assertEqual(reverse_delete("a", "a"), ('', False))
        self.assertEqual(reverse_delete("a", "b"), ('a', False))
        self.assertEqual(reverse_delete("ab", "b"), ('a', False))
        self.assertEqual(reverse_delete("abc", "b"), ('ac', False))
        self.assertEqual(reverse_delete("abcdedcba", ""), ('abcdedcba', True))
        self.assertEqual(reverse_delete("a", ""), ('a', True))
        self.assertEqual(reverse_delete("", "a"), ('', True))

if __name__ == '__main__':
    unittest.main()


This script includes 10 test cases to cover different scenarios. The test cases cover different lengths of strings, different characters in the strings, and different characters in the deletion string. The test cases also cover the edge cases where the input string is empty or the deletion string is empty.