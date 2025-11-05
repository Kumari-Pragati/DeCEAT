Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `is_happy` function:


import unittest
from HumanEval_80_code import is_happy

class TestIsHappy(unittest.TestCase):
    def test_is_happy_short_strings(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("aa"))
        self.assertFalse(is_happy(""))
        self.assertFalse(is_happy(" "))

    def test_is_happy_single_distinct_group(self):
        self.assertTrue(is_happy("abcd"))
        self.assertTrue(is_happy("xyzw"))
        self.assertTrue(is_happy("1234"))

    def test_is_happy_multiple_distinct_groups(self):
        self.assertTrue(is_happy("adb"))
        self.assertTrue(is_happy("xyyz"))
        self.assertTrue(is_happy("12345"))

    def test_is_happy_overlapping_groups(self):
        self.assertFalse(is_happy("aabb"))
        self.assertFalse(is_happy("xyy"))
        self.assertFalse(is_happy("12321"))

    def test_is_happy_empty_group(self):
        self.assertFalse(is_happy("abc"))
        self.assertFalse(is_happy("xyz"))
        self.assertFalse(is_happy("123"))

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, including short strings, single distinct groups, multiple distinct groups, overlapping groups, and empty groups. It uses the `unittest.TestCase.assertFalse()` and `unittest.TestCase.assertTrue()` methods to verify the expected output of the `is_happy()` function.