You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here's a unittest script for the given Python function:


import unittest
from HumanEval_0_code import has_close_elements

class TestHasCloseElements(unittest.TestCase):
    def test_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_single_element(self):
        self.assertFalse(has_close_elements([1.0], 0.5))

    def test_empty_list(self):
        self.assertFalse(has_close_elements([], 0.5))

    def test_negative_numbers(self):
        self.assertTrue(has_close_elements([-1.0, -0.8, 0.0, 0.2, 0.4, -0.8], 0.3))

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure that the function is working as expected. It tests the function with lists of numbers with close and non-close elements, with single elements, with empty lists, and with negative numbers.