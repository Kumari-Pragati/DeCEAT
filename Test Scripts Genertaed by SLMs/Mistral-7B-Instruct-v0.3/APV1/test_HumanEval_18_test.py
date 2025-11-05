You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `how_many_times`. The test cases cover various edge cases and ensure the function behaves as expected.


import unittest
from HumanEval_18_code import how_many_times

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_char_string(self):
        self.assertEqual(how_many_times('a', 'a'), 1)
        self.assertEqual(how_many_times('A', 'a'), 0)

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        self.assertEqual(how_many_times('bbbb', 'b'), 4)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('aaaa', 'aaa'), 1)
        self.assertEqual(how_many_times('12345', '6'), 0)

    def test_case_sensitivity(self):
        self.assertEqual(how_many_times('Hello', 'hello'), 1)
        self.assertEqual(how_many_times('HELLO', 'hello'), 1)
        self.assertEqual(how_many_times('HELLO', 'HELLO'), 1)

    def test_start_and_end_of_string(self):
        self.assertEqual(how_many_times('abc', 'c'), 2)
        self.assertEqual(how_many_times('abc', 'b'), 0)

    def test_overlapping_occurrences(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)
        self.assertEqual(how_many_times('123456', '12'), 2)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for empty strings, single character strings, multiple occurrences, substring not found, case sensitivity, start and end of string, and overlapping occurrences.