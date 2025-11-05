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

 import unittest
from HumanEval_80_code import is_happy

class TestIsHappy(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(is_happy(""))

    def test_single_character(self):
        self.assertFalse(is_happy("a"))

    def test_two_characters(self):
        self.assertFalse(is_happy("aa"))

    def test_three_distinct_characters(self):
        self.assertTrue(is_happy("abc"))

    def test_three_consecutive_identical_characters(self):
        self.assertFalse(is_happy("aaa"))

    def test_three_consecutive_identical_characters_at_end(self):
        self.assertFalse(is_happy("abcdd"))

    def test_three_consecutive_identical_characters_in_middle(self):
        self.assertFalse(is_happy("abdd"))

    def test_four_distinct_characters(self):
        self.assertTrue(is_happy("abcd"))

    def test_four_consecutive_identical_characters(self):
        self.assertFalse(is_happy("abbb"))

    def test_four_consecutive_identical_characters_at_end(self):
        self.assertFalse(is_happy("abcdd"))

    def test_four_consecutive_identical_characters_in_middle(self):
        self.assertFalse(is_happy("abdd"))

    def test_five_distinct_characters(self):
        self.assertTrue(is_happy("abcde"))

    def test_five_consecutive_identical_characters(self):
        self.assertFalse(is_happy("abcdd"))

    def test_five_consecutive_identical_characters_at_end(self):
        self.assertFalse(is_happy("abcdee"))

    def test_five_consecutive_identical_characters_in_middle(self):
        self.assertFalse(is_happy("abddd"))

    def test_six_distinct_characters(self):
        self.assertTrue(is_happy("abcdef"))

    def test_six_consecutive_identical_characters(self):
        self.assertFalse(is_happy("abcddd"))

    def test_six_consecutive_identical_characters_at_end(self):
        self.assertFalse(is_happy("abcdefe"))

    def test_six_consecutive_identical_characters_in_middle(self):
        self.assertFalse(is_happy("abddde"))

if __name__ == '__main__':
    unittest.main()