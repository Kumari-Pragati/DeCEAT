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

 Here is a unittest test script for the `sort_numbers` function:


import unittest
from HumanEval_19_code import sort_numbers

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('zero one two three four five six seven eight nine'), 'zero one two three four five six seven eight nine')
        self.assertEqual(sort_numbers('three one five'), 'one three five')
        self.assertEqual(sort_numbers('nine eight seven six five four three two one zero'), 'zero one two three four five six seven eight nine')
        self.assertEqual(sort_numbers('one zero'), 'zero one')
        self.assertEqual(sort_numbers('nine nine'), '9 9')  # Test for multiple occurrences of the same number
        self.assertEqual(sort_numbers(''), '')
        self.assertEqual(sort_numbers('nine nine a'), 'a 9 9')  # Test for non-numeric characters
        self.assertEqual(sort_numbers('one two three three'), 'one two three three')  # Test for duplicate numbers

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover various scenarios, such as multiple occurrences of the same number, non-numeric characters, and duplicate numbers. The test cases are defined in the `TestSortNumbers` class, and the test suite is run using `unittest.main()`.