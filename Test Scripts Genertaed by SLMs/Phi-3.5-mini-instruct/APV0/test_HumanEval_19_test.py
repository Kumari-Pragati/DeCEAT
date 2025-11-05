Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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

 import unittest
from HumanEval_19_code import sort_numbers

class TestSortNumbers(unittest.TestCase):

    def test_sort_numbers_empty_string(self):
        self.assertEqual(sort_numbers(''), '')

    def test_sort_numbers_single_number(self):
        self.assertEqual(sort_numbers('nine'), 'nine')

    def test_sort_numbers_multiple_numbers(self):
        self.assertEqual(sort_numbers('five three one'), 'one three five')

    def test_sort_numbers_already_sorted(self):
        self.assertEqual(sort_numbers('one two three'), 'one two three')

    def test_sort_numbers_reverse_order(self):
        self.assertEqual(sort_numbers('three five four one'), 'one four five three')

    def test_sort_numbers_mixed_case(self):
        self.assertEqual(sort_numbers('Five Three One'), 'one three five')

    def test_sort_numbers_invalid_input(self):
        with self.assertRaises(ValueError):
            sort_numbers('zero eleven')

    def test_sort_numbers_whitespace(self):
        self.assertEqual(sort_numbers(' three five '), 'three five')

if __name__ == '__main__':
    unittest.main()