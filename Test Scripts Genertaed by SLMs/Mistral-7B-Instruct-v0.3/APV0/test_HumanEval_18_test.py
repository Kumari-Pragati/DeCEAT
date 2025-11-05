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
    return times

 Here is a unittest test script for the provided function `how_many_times`. The test cases cover various scenarios, including empty strings, single characters, multiple occurrences, and overlapping substrings.


import unittest
from HumanEval_18_code import how_many_times

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_character(self):
        self.assertEqual(how_many_times('a', 'a'), 1)
        self.assertEqual(how_many_times('A', 'a'), 1)
        self.assertEqual(how_many_times('Z', 'z'), 1)

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)
        self.assertEqual(how_many_times('bananabread', 'ana'), 3)

    def test_overlapping_substring(self):
        self.assertEqual(how_many_times('aaabbaa', 'aba'), 3)
        self.assertEqual(how_many_times('aaabbaa', 'aa'), 3)
        self.assertEqual(how_many_times('aaabbaa', 'b'), 2)

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestHowManyTimes` with several test methods, each testing a specific scenario. The `unittest.main()` function is called at the end to run the tests. You can run this script directly to execute the tests.