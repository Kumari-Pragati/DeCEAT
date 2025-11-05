You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_19_code import sort_numbers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def sort_numbers(numbers: str) -> str:
    """Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return ' '.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))


### Response:
Here is a unittest test suite for the given function:


import unittest
from HumanEval_19_code import sort_numbers

class TestSortNumbers(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(sort_numbers(''), '')

    def test_single_number(self):
        self.assertEqual(sort_numbers('three'), 'three')

    def test_sorted_numbers(self):
        self.assertEqual(sort_numbers('one two three'), 'one two three')

    def test_unsorted_numbers(self):
        self.assertEqual(sort_numbers('three one two'), 'one two three')

    def test_mixed_case(self):
        self.assertEqual(sort_numbers('Three One two'), 'one Two Three')

    def test_numbers_with_spaces(self):
        self.assertEqual(sort_numbers('three  one  two'), 'one two three')

    def test_numbers_with_extra_spaces(self):
        self.assertEqual(sort_numbers('three   one     two'), 'one two three')

    def test_numbers_with_duplicates(self):
        self.assertEqual(sort_numbers('three one two three'), 'one two three three')

    def test_numbers_with_invalid_numbers(self):
        self.assertEqual(sort_numbers('three one ten'), 'one three')

if __name__ == '__main__':
    unittest.main()


This suite includes tests for empty strings, single numbers, sorted numbers, unsorted numbers, mixed case, numbers with spaces, numbers with extra spaces, numbers with duplicates, and numbers with invalid numbers.