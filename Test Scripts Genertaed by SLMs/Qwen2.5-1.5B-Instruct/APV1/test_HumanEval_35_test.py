system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):

    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

    def test_empty_list(self):
        self.assertIsNone(max_element([]))

    def test_single_element(self):
        self.assertEqual(max_element([42]), 42)

    def test_negative_numbers(self):
        self.assertEqual(max_element([-7, -2, -3, -8, -1]), -1)

    def test_large_numbers(self):
        large_numbers = [i * i for i in range(1, 1000)]
        self.assertEqual(max_element(large_numbers), 999**2)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestMaxElement` class that inherits from `unittest.TestCase`. It contains several test methods to ensure the correctness of the `max_element` function. The tests cover various scenarios including empty lists, single elements, negative numbers, and large numbers. If you run this script, it will execute all the defined tests and print whether each test passed or failed.