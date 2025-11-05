You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a unittest test suite for the provided Python function:


import unittest
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_lowercase_string(self):
        self.assertEqual(count_distinct_characters('abc'), 3)

    def test_uppercase_string(self):
        self.assertEqual(count_distinct_characters('ABC'), 3)

    def test_mixed_case_string(self):
        self.assertEqual(count_distinct_characters('AbC'), 3)

    def test_repeated_characters(self):
        self.assertEqual(count_distinct_characters('aabbcc'), 3)

    def test_single_character_string(self):
        self.assertEqual(count_distinct_characters('a'), 1)

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

if __name__ == '__main__':
    unittest.main()


This suite includes tests for various scenarios including lowercase, uppercase, mixed-case strings, strings with repeated characters, single-character strings, and empty strings. Each test verifies that the function returns the expected number of distinct characters.