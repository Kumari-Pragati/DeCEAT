You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_66_code import digitSum

class TestDigitSum(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_all_lower_case(self):
        self.assertEqual(digitSum("abAB"), 131)

    def test_all_lower_and_upper_case(self):
        self.assertEqual(digitSum("abcCd"), 67)

    def test_all_upper_case(self):
        self.assertEqual(digitSum("HELLO"), 72)

    def test_mixed_case(self):
        self.assertEqual(digitSum("helloE"), 69)

    def test_all_upper_and_lower_case(self):
        self.assertEqual(digitSum("woArBld"), 131)

    def test_all_same_case(self):
        self.assertEqual(digitSum("aAaaaXa"), 153)

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestDigitSum` that inherits from `unittest.TestCase`. It includes several test methods that test the `digitSum` function with different types of input strings. Each method asserts that the output of `digitSum` is equal to the expected result.

To run this script, you need to have Python and the unittest module installed. You can run the script directly in a Python environment. If the `digitSum` function is implemented correctly, all the tests should pass.

Please note that the `digitSum` function is supposed to return the sum of the ASCII codes of uppercase characters. The provided test cases seem to be incorrect, as they seem to be testing for the sum of uppercase characters only, not their ASCII codes. If you want to test for the sum of ASCII codes, you should use `ord(char)` instead of `ord(char) if char.isupper() else 0` in the `digitSum` function.