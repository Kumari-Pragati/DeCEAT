You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_19_code import sort_numbers

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')
        self.assertEqual(sort_numbers('five four two one'), 'one two four five')
        self.assertEqual(sort_numbers('nine eight seven six five four three two one zero'), 'zero one two three four five six seven eight nine')
        self.assertEqual(sort_numbers(''), '')
        self.assertEqual(sort_numbers('one one one one one'), 'one one one one one')
        self.assertEqual(sort_numbers('two two two two two two'), 'two two two two two two')
        self.assertEqual(sort_numbers('three two one four'), 'one two three four')
        self.assertEqual(sort_numbers('zero zero zero zero zero'), 'zero zero zero zero zero')

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestSortNumbers` with a single method `test_sort_numbers`. This method tests the `sort_numbers` function with a variety of inputs, including empty strings, strings with repeated numbers, and strings with single numbers. The `unittest.main()` call at the end runs these tests.

Please note that you need to have the `HumanEval_19_code` module available in the same directory or in your PYTHONPATH. If it's not, you need to replace `from HumanEval_19_code import sort_numbers` with the actual code of the `sort_numbers` function.