You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function:


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
        self.assertEqual(unique([1, 'a', 2, 'a', 3]), [1, 'a', 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(unique([-1, 0, 1]), [-1, 0, 1])

    def test_large_numbers(self):
        self.assertEqual(unique([123, 456, 789, 123]), [123, 456, 789])

    def test_multiple_lists(self):
        self.assertEqual(unique([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) , [1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to check the function's behavior with empty lists, single elements, duplicate elements, mixed data types, negative numbers, large numbers, and multiple lists.