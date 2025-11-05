You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 import unittest
from HumanEval_34_code import unique

class TestUniqueFunction(unittest.TestCase):

    def test_unique_with_duplicates(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

    def test_unique_empty_list(self):
        self.assertEqual(unique([]), [])

    def test_unique_single_element(self):
        self.assertEqual(unique([1]), [1])

    def test_unique_sorted_list(self):
        self.assertEqual(unique([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unique_with_negative_numbers(self):
        self.assertEqual(unique([-3, -1, -1, -2, -3]), [-3, -2, -1])

    def test_unique_with_mixed_types(self):
        with self.assertRaises(TypeError):
            unique([1, "two", 3.0, "three"])

if __name__ == '__main__':
    unittest.main()