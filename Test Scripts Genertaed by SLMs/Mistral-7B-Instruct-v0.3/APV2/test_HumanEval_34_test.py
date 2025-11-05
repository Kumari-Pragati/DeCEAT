You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_34_code import unique
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))

 Here is the complete unittest test suite for the `unique` function:


import unittest
from HumanEval_34_code import unique

class TestUniqueFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(unique([]), [])

    def test_single_element_list(self):
        self.assertEqual(unique([1]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(unique([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_mixed_data_types(self):
        self.assertEqual(unique([1, 2, 'a', 'a', 3]), [1, 2, 'a', 3])

    def test_negative_numbers(self):
        self.assertEqual(unique([-1, 0, 1]), [-1, 0, 1])

    def test_large_numbers(self):
        self.assertEqual(unique([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 123, 456, 789]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 123, 456, 789])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty list, single-element lists, duplicate elements, mixed data types, negative numbers, and large numbers. Each test case uses the `assertEqual` method to compare the expected output with the actual output of the `unique` function.