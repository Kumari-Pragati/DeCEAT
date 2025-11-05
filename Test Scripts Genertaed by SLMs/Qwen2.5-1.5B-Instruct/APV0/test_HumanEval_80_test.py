system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return True


assistant

import unittest

# Importing the function we want to test
from HumanEval_80_code import is_happy

class TestIsHappy(unittest.TestCase):

    def test_is_happy(self):
        self.assertEqual(is_happy("a"), False)
        self.assertEqual(is_happy("aa"), False)
        self.assertEqual(is_happy("abcd"), True)
        self.assertEqual(is_happy("aabb"), False)
        self.assertEqual(is_happy("adb"), True)
        self.assertEqual(is_happy("xyy"), False)

if __name__ == '__main__':
    unittest.main()


This script imports the `is_happy` function from the `HumanEval_80_code` module and defines a class `TestIsHappy` that inherits from `unittest.TestCase`. It contains a method `test_is_happy` which tests various cases of the `is_happy` function using assertions. If all tests pass, it will run the entire test suite when executed as a standalone program.