You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_22_code import filter_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """Filter given list of any Python values only for integers.
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]


### Response:
Here is a unittest test suite for the filter_integers function:


import unittest
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):

    def test_filter_integers(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])
        self.assertEqual(filter_integers([1, 'two', 3.0, 'four', 5]), [1, 5])
        self.assertEqual(filter_integers([True, False, 0, 1]), [0, 1])
        self.assertEqual(filter_integers([None]), [])
        self.assertEqual(filter_integers([]), [])
        self.assertEqual(filter_integers([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios, including:

- A list with some integers and other types
- A list with boolean values and integers
- A list with None and an integer
- An empty list
- A list with only integers

Each test case checks if the output of the filter_integers function matches the expected result.