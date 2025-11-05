You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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

 
import unittest
from HumanEval_66_code import digitSum

class TestDigitSum(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_single_uppercase(self):
        self.assertEqual(digitSum("A"), 65)

    def test_multiple_uppercase(self):
        self.assertEqual(digitSum("AB"), 65 + 66)

    def test_mixed_case(self):
        self.assertEqual(digitSum("abAB"), 66 + 66)

    def test_lowercase_only(self):
        self.assertEqual(digitSum("abcCd"), 67)

    def test_single_uppercase_with_lowercase(self):
        self.assertEqual(digitSum("helloE"), 69)

    def test_mixed_case_with_lowercase(self):
        self.assertEqual(digitSum("woArBld"), 69 + 65 + 66)

    def test_multiple_uppercase_with_lowercase(self):
        self.assertEqual(digitSum("aAaaaXa"), 65 + 65 + 65 + 66)

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases for the `digitSum` function, including empty strings, strings with a single uppercase letter, strings with multiple uppercase letters, strings with mixed case, and strings with both uppercase and lowercase letters. Each test case asserts that the function returns the correct sum of the ASCII values of the uppercase characters in the input string.