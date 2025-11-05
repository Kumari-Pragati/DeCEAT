You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_18_code import how_many_times

class TestHowManyTimes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_char_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_overlapping_substring(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_non_overlapping_substring(self):
        self.assertEqual(how_many_times('aaaa', 'aaa'), 1)

    def test_substring_not_in_string(self):
        self.assertEqual(how_many_times('abc', 'd'), 0)

    def test_empty_substring(self):
        self.assertEqual(how_many_times('abc', ''), 3)

if __name__ == '__main__':
    unittest.main()


This script creates a test case class `TestHowManyTimes` that inherits from `unittest.TestCase`. It includes several test methods that test different scenarios, including empty strings, single character substrings, overlapping substrings, non-overlapping substrings, substrings not in the string, and empty substrings. Each method asserts that the output of `how_many_times` matches the expected result.

Please note that the `HumanEval_18_code` module should contain the `how_many_times` function for these tests to work. If the function is defined in a different module, you should replace `from HumanEval_18_code import how_many_times` with the appropriate import statement.