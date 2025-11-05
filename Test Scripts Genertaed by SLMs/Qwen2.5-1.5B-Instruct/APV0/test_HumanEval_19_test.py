system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Define the function to be tested
from HumanEval_19_code import sort_numbers

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        # Test case 1: Correctly sorts numbers between 'zero' and 'nine'
        self.assertEqual(sort_numbers('three one five'), 'one three five')

        # Test case 2: Handles an empty input
        self.assertEqual(sort_numbers(""), "")

        # Test case 3: Handles a single number input
        self.assertEqual(sort_numbers('nine'), 'nine')

        # Test case 4: Handles multiple spaces as separators
        self.assertEqual(sort_numbers('two four six eight'), 'two four six eight')

        # Test case 5: Handles mixed inputs (e.g., 'ten two')
        self.assertEqual(sort_numbers('ten two'), 'two ten')

        # Test case 6: Handles negative numbers (e.g., '-three')
        self.assertEqual(sort_numbers('-three'), '-three')

if __name__ == '__main__':
    unittest.main()


This script defines a `TestSortNumbers` class that inherits from `unittest.TestCase`. It contains several test cases to ensure the `sort_numbers` function works correctly under various conditions. The `assertEqual` method is used to compare the expected output with the actual output of the function. If any test fails, it will raise an assertion error, indicating which test failed and why.