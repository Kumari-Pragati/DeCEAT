You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):
    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)
        self.assertEqual(max_element([-1, -2, -3]), -1)
        self.assertEqual(max_element([1]), 1)
        self.assertEqual(max_element([]), None)
        self.assertIsNone(max_element([]))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios such as when the maximum element is at the beginning, end, or middle of the list, when there is only one element in the list, and when the list is empty. It also checks that the function returns None when the list is empty.