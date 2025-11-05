system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_23_code import strlen
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


assistant

import unittest

# Importing the function to be tested
from HumanEval_23_code import strlen

class TestStringLength(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)
        
    def test_single_character_string(self):
        self.assertEqual(strlen("a"), 1)
        
    def test_multiple_characters_string(self):
        self.assertEqual(strlen("hello"), 5)
        
    def test_whitespace_string(self):
        self.assertEqual(strlen("   "), 1)
        
    def test_special_characters_string(self):
        self.assertEqual(strlen("!@#$%^&*()"), 10)

if __name__ == '__main__':
    unittest.main()


This script imports the `strlen` function and defines several test cases using the `unittest.TestCase` class. Each method in this class is a test case that uses assertions to check if the `strlen` function returns the expected results for different types of input strings. The `unittest.main()` call at the end makes sure all tests can run when the script is executed directly.