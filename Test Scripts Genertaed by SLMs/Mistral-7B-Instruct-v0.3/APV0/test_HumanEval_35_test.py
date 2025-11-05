Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_35_code import max_element
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m

 Here is a simple unittest test script for the `max_element` function. I've added some test cases to cover various scenarios, including an empty list, a list with negative numbers, and a list with multiple maximum elements.


import unittest
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_element([]), None)

    def test_single_element(self):
        self.assertEqual(max_element([1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(max_element([1, 2, 3]), 3)

    def test_negative_numbers(self):
        self.assertEqual(max_element([-1, -2, -3]), -1)

    def test_multiple_maximum_elements(self):
        self.assertEqual(max_element([1, 2, 2, 3]), 3)
        self.assertEqual(max_element([3, 2, 2, 1]), 3)

if __name__ == '__main__':
    unittest.main()


This script includes a test case for an empty list, a single-element list, a list with multiple elements, a list with negative numbers, and a list with multiple maximum elements. You can run this script directly to test your `max_element` function.