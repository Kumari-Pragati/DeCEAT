You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_28_code import concatenate

class TestConcatenate(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_single_string(self):
        self.assertEqual(concatenate(['a']), 'a')

    def test_multiple_strings(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_mixed_strings(self):
        self.assertEqual(concatenate(['a1', 'b2', 'c3']), 'a1b2c3')

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            concatenate(['a', 1, 'b'])

    def test_large_string_list(self):
        self.assertEqual(concatenate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']), 'abcdefghijklmnopqrstuvwxyz')

if __name__ == '__main__':
    unittest.main()