You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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

class TestConcatenateFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_single_string(self):
        self.assertEqual(concatenate(['a']), 'a')

    def test_multiple_strings(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_mixed_case_strings(self):
        self.assertEqual(concatenate(['A', 'b', 'C']), 'ABC')

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            concatenate(['a', 1, 'c'])

    def test_large_string_list(self):
        large_strings = ['string' * i for i in range(100)]
        concatenated_string = ''.join(large_strings)
        self.assertEqual(concatenate(large_strings), concatenated_string)

if __name__ == '__main__':
    unittest.main()