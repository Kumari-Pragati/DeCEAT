Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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

    def test_unique_with_empty_list(self):
        self.assertEqual(unique([]), [])

    def test_unique_with_single_element(self):
        self.assertEqual(unique([42]), [42])

    def test_unique_with_negative_numbers(self):
        self.assertEqual(unique([-1, -2, -1, -2, -3]), [-3, -1, -2])

    def test_unique_with_mixed_types(self):
        self.assertEqual(unique([1, 'a', 1.0, 'a']), [1, 1.0])

    def test_unique_with_none_and_empty_string(self):
        self.assertEqual(unique([None, '', ' ', 'hello']), ['', ' ', 'hello'])

    def test_unique_with_complex_numbers(self):
        self.assertEqual(unique([3+4j, 3+4j, 1+2j]), [3+4j, 1+2j])

if __name__ == '__main__':
    unittest.main()