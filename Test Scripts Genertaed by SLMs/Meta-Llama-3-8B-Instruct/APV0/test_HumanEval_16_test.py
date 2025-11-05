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

    return len(set(string.lower()))assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_count_distinct_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)
        self.assertEqual(count_distinct_characters(''), 0)
        self.assertEqual(count_distinct_characters('a'), 1)
        self.assertEqual(count_distinct_characters('abc'), 3)
        self.assertEqual(count_distinct_characters('abcabc'), 3)
        self.assertEqual(count_distinct_characters('aA'), 2)
        self.assertEqual(count_distinct_characters('aAaA'), 2)
        self.assertEqual(count_distinct_characters('aAaAaA'), 2)
        self.assertEqual(count_distinct_characters('aAaAaAaA'), 2)

if __name__ == '__main__':
    unittest.main()


This script includes a variety of test cases to ensure the function is working correctly. The test cases include strings with different lengths, characters, and cases. The `assertEqual` method is used to compare the expected output with the actual output of the function.