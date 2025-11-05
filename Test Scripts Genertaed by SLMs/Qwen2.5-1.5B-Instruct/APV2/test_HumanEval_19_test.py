system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Provided function to be tested
from HumanEval_19_code import sort_numbers

class TestSortNumbers(unittest.TestCase):
    
    def test_sort_numbers(self):
        # Test case 1: Simple input
        self.assertEqual(sort_numbers('three one five'), 'one three five')
        
        # Test case 2: Input with multiple digits
        self.assertEqual(sort_numbers('ten nine eight seven six five four three two one zero'), 
                         'one two three four five six seven eight nine ten')
        
        # Test case 3: Empty input
        self.assertEqual(sort_numbers(''), '')
        
        # Test case 4: Single digit input
        self.assertEqual(sort_numbers('nine'), 'nine')
        
        # Test case 5: Mixed inputs (should raise ValueError)
        with self.assertRaises(ValueError):
            sort_numbers('eleven twelve thirteen')

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure that `sort_numbers` function behaves as expected under various conditions, including handling empty strings and mixed inputs.