system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Provided code
from HumanEval_18_code import how_many_times


class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_char_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('hello world', 'o'), 2)
        self.assertEqual(how_many_times('test test test', 't'), 3)

    def test_case_insensitive(self):
        self.assertEqual(how_many_times('Hello World', 'world'), 1)


if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure that `how_many_times` function works correctly under various conditions, including empty strings, single character substrings, multiple occurrences of the substring, and case-insensitivity.