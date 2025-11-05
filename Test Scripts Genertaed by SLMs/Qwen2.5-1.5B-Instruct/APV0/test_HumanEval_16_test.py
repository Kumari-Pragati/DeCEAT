system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_16_code import count_distinct_characters
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    return len(set(string.lower()))


assistant

import unittest

# Importing the function to be tested
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):
    
    def test_count_distinct_characters(self):
        # Test cases provided in the problem description
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

    def test_empty_string(self):
        # Test an empty string
        self.assertEqual(count_distinct_characters(""), 0)

    def test_single_char(self):
        # Test a single character string
        self.assertEqual(count_distinct_characters("a"), 1)

    def test_all_same_case(self):
        # Test strings where all characters are the same case
        self.assertEqual(count_distinct_characters('aaaa'), 1)
        self.assertEqual(count_distinct_characters('ZZZz'), 1)

if __name__ == '__main__':
    unittest.main()


This script imports the `count_distinct_characters` function and defines several test cases using the `unittest.TestCase` class. It includes assertions to check if the function returns the expected results for different inputs, such as an empty string, a single character string, and strings with all characters being the same case. The `unittest.main()` call at the end makes the tests executable when run directly.