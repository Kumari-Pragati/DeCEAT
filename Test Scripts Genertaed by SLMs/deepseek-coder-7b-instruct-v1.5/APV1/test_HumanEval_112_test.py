You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_112_code import reverse_delete

class TestReverseDelete(unittest.TestCase):

    def test_reverse_delete(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))
        self.assertEqual(reverse_delete("aabbcc", "abc"), ('', True))
        self.assertEqual(reverse_delete("abcabc", "abc"), ('', True))
        self.assertEqual(reverse_delete("abcabc", "b"), ('acac', False))
        self.assertEqual(reverse_delete("abcabc", ""), ('abcabc', True))
        self.assertEqual(reverse_delete("", "abc"), ('', True))
        self.assertEqual(reverse_delete("", ""), ('', True))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various scenarios, including when the string `s` is empty, when the string `c` is empty, and when the string `s` contains characters that are not in string `c`.