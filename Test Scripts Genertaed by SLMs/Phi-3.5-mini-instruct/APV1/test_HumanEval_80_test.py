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

 import unittest
from HumanEval_80_code import is_happy

class TestIsHappy(unittest.TestCase):
    def test_short_string(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("aa"))

    def test_happy_string(self):
        self.assertTrue(is_happy("abcd"))
        self.assertTrue(is_happy("adb"))

    def test_unhappy_string_length_less_than_three(self):
        self.assertFalse(is_happy("ab"))
        self.assertFalse(is_happy(""))

    def test_unhappy_string_repeated_letters(self):
        self.assertFalse(is_happy("aabb"))
        self.assertFalse(is_happy("xyy"))
        self.assertFalse(is_happy("aaa"))
        self.assertFalse(is_happy("abcabc"))

    def test_unhappy_string_non_alphabetic(self):
        self.assertFalse(is_happy("123"))
        self.assertFalse(is_happy("!@#"))

    def test_happy_string_with_spaces(self):
        self.assertTrue(is_happy("abc d"))

    def test_happy_string_with_uppercase(self):
        self.assertTrue(is_happy("AbC"))

if __name__ == '__main__':
    unittest.main()