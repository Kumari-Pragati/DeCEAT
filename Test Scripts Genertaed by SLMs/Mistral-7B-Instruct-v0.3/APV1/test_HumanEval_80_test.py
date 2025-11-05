You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_80_code import is_happy

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

    Examples:
        is_happy("a") => False
        is_happy("aa") => False
        is_happy("abcd") => True
        is_happy("aabb") => False
        is_happy("adb") => True
        is_happy("xyy") => False
    """

    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i] == s[i + 2]:
            return False
    return True

 Here is a comprehensive unittest test suite for the given Python function `is_happy`.


import unittest
from HumanEval_80_code import is_happy

class TestIsHappy(unittest.TestCase):

    def test_is_happy_empty_string(self):
        self.assertFalse(is_happy(""))

    def test_is_happy_single_char(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("A"))
        self.assertFalse(is_happy("0"))
        self.assertFalse(is_happy(" "))

    def test_is_happy_two_chars(self):
        self.assertFalse(is_happy("aa"))
        self.assertFalse(is_happy("ab"))
        self.assertFalse(is_happy("AB"))
        self.assertFalse(is_happy("00"))
        self.assertFalse(is_happy("  "))

    def test_is_happy_three_chars(self):
        self.assertTrue(is_happy("abc"))
        self.assertTrue(is_happy("ABC"))
        self.assertTrue(is_happy("123"))
        self.assertTrue(is_happy("xyz"))
        self.assertTrue(is_happy("XYZ"))

    def test_is_happy_four_chars(self):
        self.assertTrue(is_happy("abcd"))
        self.assertTrue(is_happy("ABCD"))
        self.assertTrue(is_happy("1234"))
        self.assertTrue(is_happy("xyzw"))
        self.assertTrue(is_happy("XYZW"))

    def test_is_happy_five_chars(self):
        self.assertTrue(is_happy("abcde"))
        self.assertTrue(is_happy("ABCDE"))
        self.assertTrue(is_happy("12345"))
        self.assertTrue(is_happy("xyzwa"))
        self.assertTrue(is_happy("XYZWA"))

    def test_is_happy_duplicates(self):
        self.assertFalse(is_happy("aaa"))
        self.assertFalse(is_happy("aab"))
        self.assertFalse(is_happy("AAB"))
        self.assertFalse(is_happy("000"))
        self.assertFalse(is_happy("  a "))

    def test_is_happy_longer_strings(self):
        self.assertTrue(is_happy("abcdefg"))
        self.assertTrue(is_happy("ABCDEFG"))
        self.assertTrue(is_happy("1234567"))
        self.assertTrue(is_happy("xyzwvut"))
        self.assertTrue(is_happy("XYZWVUT"))

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases for different lengths of strings and cases where the three consecutive characters are not distinct. It also covers edge cases such as empty strings, single characters, and strings with duplicates.