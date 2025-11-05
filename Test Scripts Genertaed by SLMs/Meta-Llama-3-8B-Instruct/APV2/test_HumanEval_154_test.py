system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_154_code import cycpattern_check
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i + l] == pat[j:j + l]:
                return True
    return Falseassistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_154_code import cycpattern_check

class TestCycpatternCheck(unittest.TestCase):

    def test_cycpattern_check(self):
        self.assertFalse(cycpattern_check("abcd", "abd"))
        self.assertTrue(cycpattern_check("hello", "ell"))
        self.assertFalse(cycpattern_check("whassup", "psus"))
        self.assertTrue(cycpattern_check("abab", "baa"))
        self.assertFalse(cycpattern_check("efef", "eeff"))
        self.assertTrue(cycpattern_check("himenss", "simen"))

if __name__ == '__main__':
    unittest.main()