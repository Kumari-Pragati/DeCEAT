system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return sum(ord(char) if char.isupper() else 0 for char in s)


assistant

import unittest

# Function to be tested
from HumanEval_66_code import digitSum

class TestDigitSum(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)
    
    def test_single_char(self):
        self.assertEqual(digitSum("a"), 97)
    
    def test_multiple_chars(self):
        self.assertEqual(digitSum("abc"), 97 + 98 + 99)
    
    def test_uppercase_only(self):
        self.assertEqual(digitSum("HELLO"), 72 + 69 + 76 + 79)
    
    def test_mixed_case(self):
        self.assertEqual(digitSum("AbcD"), 97 + 98 + 99 + 100)
    
    def test_all_lowercase(self):
        self.assertEqual(digitSum("xyz"), 94 + 99 + 105)
    
    def test_no_uppercase(self):
        self.assertEqual(digitSum("abcd"), 97 + 98 + 99 + 100)
    
    def test_all_uppercase(self):
        self.assertEqual(digitSum("ABCDEFGH"), 65 * 8)

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a class `TestDigitSum` with methods to test various cases of the `digitSum` function. It includes assertions to check the correctness of the function against different inputs. The `if __name__ == '__main__':` block ensures that the tests can be run directly when the module is executed.