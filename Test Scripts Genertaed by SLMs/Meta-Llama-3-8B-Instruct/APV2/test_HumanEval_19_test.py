system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight', and 'nine'.
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
    return''.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))assistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_19_code import sort_numbers

class TestSortNumbers(unittest.TestCase):

    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('zero one two'), 'one two zero')
        self.assertEqual(sort_numbers('five seven nine'), 'five seven nine')
        self.assertEqual(sort_numbers('three one five'), 'one three five')
        self.assertEqual(sort_numbers('eight six four'), 'four six eight')
        self.assertEqual(sort_numbers('nine eight seven'),'seven eight nine')
        self.assertEqual(sort_numbers('two zero'), 'two zero')
        self.assertEqual(sort_numbers('one'), 'one')
        self.assertEqual(sort_numbers(''), '')
        self.assertEqual(sort_numbers('zero'), 'zero')
        self.assertEqual(sort_numbers('one two three four five six seven eight nine'), 
                         'eight nine seven six five four three two one zero')

if __name__ == '__main__':
    unittest.main()