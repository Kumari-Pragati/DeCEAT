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

 import unittest
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):
    def test_max_element_with_positive_integers(self):
        self.assertEqual(max_element([1, 2, 3]), 3)

    def test_max_element_with_negative_integers(self):
        self.assertEqual(max_element([-5, -3, -10]), -3)

    def test_max_element_with_mixed_integers(self):
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

    def test_max_element_with_empty_list(self):
        self.assertEqual(max_element([]), None)

    def test_max_element_with_single_element_list(self):
        self.assertEqual(max_element([5]), 5)

    def test_max_element_with_all_elements_equal(self):
        self.assertEqual(max_element([2, 2, 2, 2]), 2)

    def test_max_element_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            max_element([1, "two", 3])

if __name__ == '__main__':
    unittest.main()