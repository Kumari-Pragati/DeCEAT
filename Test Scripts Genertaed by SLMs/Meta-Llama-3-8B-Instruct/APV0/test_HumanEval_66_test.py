user

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
    return sum(ord(char) if char.isupper() else 0 for char in s)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_66_code import digitSum

class TestDigitSum(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_single_uppercase_character(self):
        self.assertEqual(digitSum("A"), 65)

    def test_multiple_uppercase_characters(self):
        self.assertEqual(digitSum("ABC"), 130)

    def test_multiple_characters_with_mixed_case(self):
        self.assertEqual(digitSum("aAbBcC"), 156)

    def test_string_with_no_uppercase_characters(self):
        self.assertEqual(digitSum("hello"), 0)

    def test_string_with_no_characters(self):
        self.assertEqual(digitSum(""), 0)

if __name__ == '__main__':
    unittest.main()


This script includes tests for the following scenarios:
- An empty string
- A string with a single uppercase character
- A string with multiple uppercase characters
- A string with a mix of uppercase and lowercase characters
- A string with no uppercase characters
- A string with no characters

Each test case checks if the output of the `digitSum` function matches the expected output.