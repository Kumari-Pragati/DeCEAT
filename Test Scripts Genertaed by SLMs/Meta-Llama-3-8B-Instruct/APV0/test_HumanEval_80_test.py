user

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
    return Trueassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_80_code import is_happy

class TestIsHappy(unittest.TestCase):

    def test_happy_string(self):
        self.assertTrue(is_happy("abcd"))
        self.assertTrue(is_happy("adb"))
        self.assertTrue(is_happy("xyz"))

    def test_not_happy_string(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("aa"))
        self.assertFalse(is_happy("aabb"))
        self.assertFalse(is_happy("xyy"))

    def test_edge_cases(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("abc"))
        self.assertTrue(is_happy("abcabc"))

if __name__ == '__main__':
    unittest.main()


This script includes three test cases:

- `test_happy_string`: Tests strings that are expected to be happy.
- `test_not_happy_string`: Tests strings that are expected to be not happy.
- `test_edge_cases`: Tests edge cases, such as strings with lengths less than 3.

Each test case includes assertions to verify the expected output of the `is_happy` function.