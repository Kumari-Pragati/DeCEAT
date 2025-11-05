You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `how_many_times` function:


import unittest
from HumanEval_18_code import how_many_times

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_character_string(self):
        self.assertEqual(how_many_times('a', 'a'), 1)
        self.assertEqual(how_many_times('A', 'a'), 1)
        self.assertEqual(how_many_times('0', '0'), 1)

    def test_multiple_characters_string(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)
        self.assertEqual(how_many_times('ababab', 'ab'), 3)
        self.assertEqual(how_many_times('ABCABC', 'AB'), 2)
        self.assertEqual(how_many_times('123123', '12'), 2)

    def test_case_insensitive(self):
        self.assertEqual(how_many_times('aaa', 'A'), 3)
        self.assertEqual(how_many_times('ABCABC', 'Ab'), 2)
        self.assertEqual(how_many_times('123123', '12'), 2)

    def test_edge_cases(self):
        self.assertEqual(how_many_times('', 'a'), 0)
        self.assertEqual(how_many_times('a', ''), 0)
        self.assertEqual(how_many_times('aa', 'a'), 2)
        self.assertEqual(how_many_times('aa', 'aa'), 1)
        self.assertEqual(how_many_times('aaa', 'aa'), 1)
        self.assertEqual(how_many_times('aaa', 'aaa'), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, including empty strings, single-character strings, multiple-character strings, case-insensitive strings, and edge cases.