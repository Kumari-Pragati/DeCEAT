You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a simple unittest test suite for the `max_element` function:


import unittest
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_element([]), None)

    def test_single_element_list(self):
        self.assertEqual(max_element([1]), 1)
        self.assertEqual(max_element([-1]), -1)
        self.assertEqual(max_element([0]), 0)

    def test_simple_list(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

    def test_negative_numbers(self):
        self.assertEqual(max_element([-5, -3, -2, -1]), -1)
        self.assertEqual(max_element([-5, 3, -2, -1]), 3)

    def test_floats(self):
        self.assertEqual(max_element([3.14, 2.718, 1.618]), 3.14)
        self.assertEqual(max_element([-3.14, -2.718, -1.618]), -1.618)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty list, a single-element list, lists with positive and negative numbers, and lists with floats. The test suite uses the `unittest.TestCase` class to define test methods with the `test_` prefix, and the `assertEqual` method to check the expected and actual results.