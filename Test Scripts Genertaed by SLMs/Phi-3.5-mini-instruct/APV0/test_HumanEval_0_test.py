Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_0_code import has_close_elements
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False

 import unittest
from HumanEval_0_code import has_close_elements

class TestHasCloseElements(unittest.TestCase):

    def test_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_close_elements_found(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_empty_list(self):
        self.assertFalse(has_close_elements([], 0.5))

    def test_single_element_list(self):
        self.assertFalse(has_close_elements([1.0], 0.5))

    def test_all_elements_close(self):
        self.assertTrue(has_close_elements([1.0, 1.1, 1.2, 1.3], 0.1))

    def test_large_numbers(self):
        self.assertFalse(has_close_elements([1000.0, 1001.0, 1002.0], 0.001))

    def test_negative_numbers(self):
        self.assertFalse(has_close_elements([-1.0, -2.0, -3.0], 0.5))

    def test_zero_threshold(self):
        self.assertTrue(has_close_elements([1.0, 2.0, 3.0], 0))

    def test_zero_numbers(self):
        self.assertFalse(has_close_elements([], 0.5))

if __name__ == '__main__':
    unittest.main()