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

 import unittest
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_single_case_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)

    def test_mixed_case_characters(self):
        self.assertEqual(count_distinct_characters('Jerry'), 4)

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters('a'), 1)

    def test_no_distinct_characters(self):
        self.assertEqual(count_distinct_characters('aaaa'), 1)

    def test_whitespace_and_punctuation(self):
        self.assertEqual(count_distinct_characters('Hello, World!'), 10)

if __name__ == '__main__':
    unittest.main()