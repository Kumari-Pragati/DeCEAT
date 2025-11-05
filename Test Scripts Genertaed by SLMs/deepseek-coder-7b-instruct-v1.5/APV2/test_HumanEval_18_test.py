You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_18_code import how_many_times

class TestHowManyTimes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_character_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_multiple_character_substring(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_substring_not_in_string(self):
        self.assertEqual(how_many_times('abc', 'd'), 0)

    def test_overlapping_substring(self):
        self.assertEqual(how_many_times('aaaaa', 'aa'), 4)

    def test_empty_substring(self):
        self.assertEqual(how_many_times('abc', ''), 3)

    def test_string_longer_than_substring(self):
        self.assertEqual(how_many_times('abcdef', 'abc'), 1)

    def test_string_same_length_as_substring(self):
        self.assertEqual(how_many_times('abc', 'abc'), 1)

    def test_string_shorter_than_substring(self):
        self.assertEqual(how_many_times('ab', 'abc'), 0)

if __name__ == '__main__':
    unittest.main()


This suite includes tests for various edge cases, such as empty strings, single-character substrings, multiple-character substrings, substrings not in the string, overlapping substrings, empty substrings, strings longer than the substring, strings the same length as the substring, and strings shorter than the substring.