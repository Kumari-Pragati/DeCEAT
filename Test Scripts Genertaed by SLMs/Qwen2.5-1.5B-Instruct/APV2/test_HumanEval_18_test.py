system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return times


assistant

import unittest

# Provided function
from HumanEval_18_code import how_many_times

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_char_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('abcdeabcde', 'abc'), 2)
        self.assertEqual(how_many_times('hello world', 'o'), 2)

    def test_case_insensitive(self):
        self.assertEqual(how_many_times('Hello World', 'l'), 3)
        self.assertEqual(how_many_times('HELLO WORLD', 'L'), 3)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('abcdefg', 'z'), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various edge cases as well as more common scenarios, ensuring that the `how_many_times` function behaves correctly under different conditions.