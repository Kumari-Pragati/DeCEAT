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

 Here is a unittest test script for the `count_distinct_characters` function:


import unittest
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_count_distinct_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)
        self.assertEqual(count_distinct_characters('aA1B2cC3'), 6)
        self.assertEqual(count_distinct_characters(''), 0)
        self.assertEqual(count_distinct_characters('abcdefghijklmnopqrstuvwxyz'), 26)
        self.assertEqual(count_distinct_characters('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 26)
        self.assertEqual(count_distinct_characters('abc123!@#$%^&*()'), 10)
        self.assertEqual(count_distinct_characters('Hello, World!'), 16)
        self.assertEqual(count_distinct_characters('Hello, World!Hello, World!'), 16)

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to ensure the function works correctly for different inputs. It checks the function's behavior with empty strings, strings containing only lowercase letters, strings containing only uppercase letters, strings containing numbers and special characters, and strings containing repeated characters.