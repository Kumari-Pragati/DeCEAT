user

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
    return massistant

Here is the unittest test script for the `max_element` function:

import unittest
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(max_element([1]), 1)

    def test_single_element_list_with_negative(self):
        self.assertEqual(max_element([-1]), -1)

    def test_multiple_elements_list(self):
        self.assertEqual(max_element([1, 2, 3]), 3)

    def test_multiple_elements_list_with_negative(self):
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            max_element([])

    def test_list_with_no_elements_greater_than_first(self):
        self.assertEqual(max_element([1, 1, 1, 1]), 1)

if __name__ == '__main__':
    unittest.main()

This test script covers the following scenarios:

1. A list with a single element
2. A list with a single negative element
3. A list with multiple elements
4. A list with multiple elements, including negative numbers
5. An empty list (which should raise an IndexError)
6. A list with no elements greater than the first element

Each test method uses the `assertEqual` method to verify that the output of the `max_element` function matches the expected result. For the empty list test, we use the `assertRaises` method to verify that an IndexError is raised when calling the function with an empty list.