You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_27_code import flip_case

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()

 Here is a simple unittest test suite for the `flip_case` function:


import unittest
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):

    def test_flip_case_simple_string(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')

    def test_flip_case_mixed_case_string(self):
        self.assertEqual(flip_case('HeLlo WoRlD'), 'hELLo wORlD')

    def test_flip_case_empty_string(self):
        self.assertEqual(flip_case(''), '')

    def test_flip_case_single_character_string(self):
        self.assertEqual(flip_case('a'), 'A')
        self.assertEqual(flip_case('A'), 'a')

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases for different scenarios:

1. A simple string with only lowercase characters.
2. A mixed case string with both lowercase and uppercase characters.
3. An empty string.
4. A single character string with both lowercase and uppercase characters.

Each test case uses the `assertEqual` method to compare the expected output with the actual output of the `flip_case` function. If the function works correctly, the test will pass; otherwise, it will fail and provide an error message to help you debug the issue.