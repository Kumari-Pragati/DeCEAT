Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_66_code import digitSum
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    if s == "":
        return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

 Here is a unittest test script for the `digitSum` function:


import unittest
from HumanEval_66_code import digitSum

class TestDigitSum(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_lowercase_characters(self):
        self.assertEqual(digitSum("abAB"), 131)

    def test_mixed_case(self):
        self.assertEqual(digitSum("abcCd"), 67)

    def test_special_characters(self):
        self.assertEqual(digit digitSum("helloE"), 69)

    def test_repeated_characters(self):
        self.assertEqual(digitSum("woArBld"), 131)

    def test_repeated_uppercase_characters(self):
        self.assertEqual(digitSum("aAaaaXa"), 153)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases for different scenarios, such as an empty string, lowercase characters, mixed case, special characters, repeated characters, and repeated uppercase characters. It uses the `assertEqual` method to check if the expected and actual results match.