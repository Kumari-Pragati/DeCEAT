user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_18_code import how_many_times
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def how_many_times(string: str, substring: str) -> int:
    """Find how many times a given substring can be found in the original string. Count overlapping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    times = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            times += 1
    return timesassistant

Here is a unittest test script for the `how_many_times` function:

Python
import unittest
from HumanEval_18_code import how_many_times

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_char(self):
        self.assertEqual(how_many_times('a', 'a'), 1)
        self.assertEqual(how_many_times('a', 'b'), 0)

    def test_multiple_chars(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)
        self.assertEqual(how_many_times('abc', 'ab'), 1)

    def test_substring_longer_than_string(self):
        self.assertEqual(how_many_times('a', 'abc'), 0)

    def test_substring_overlapping(self):
        self.assertEqual(how_many_times('abcdef', 'ab'), 2)
        self.assertEqual(how_many_times('abcdef', 'abc'), 1)

if __name__ == '__main__':
    unittest.main()


This test script includes tests for the following scenarios:
- An empty string
- A single character
- Multiple characters
- A substring longer than the string
- Overlapping cases

Each test case checks if the function returns the expected result.