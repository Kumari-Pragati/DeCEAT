You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_28_code import concatenate
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def concatenate(strings: List[str]) -> str:
    """Concatenate list of strings into a single string.
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_28_code import concatenate

class TestConcatenate(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_single_string(self):
        self.assertEqual(concatenate(['a']), 'a')

    def test_multiple_strings(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_duplicate_strings(self):
        self.assertEqual(concatenate(['a', 'a', 'b', 'b']), 'aab')

    def test_mixed_case_strings(self):
        self.assertEqual(concatenate(['A', 'b', 'C']), 'ABC')

    def test_numeric_strings(self):
        self.assertEqual(concatenate(['1', '2', '3']), '123')

    def test_special_characters(self):
        self.assertEqual(concatenate(['!', '@', '#']), '!@#')

if __name__ == '__main__':
    unittest.main()


This script creates a unittest test case for the `concatenate` function. It tests the function with different types of input, including empty lists, single strings, multiple strings, duplicate strings, strings with mixed case, numeric strings, and strings with special characters.

Please note that you need to have the `HumanEval_28_code` module and the `concatenate` function defined in it for this script to work.