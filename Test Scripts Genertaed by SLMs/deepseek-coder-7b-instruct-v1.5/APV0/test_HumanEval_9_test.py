You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_9_code import rolling_max
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """Return a list where each element is the maximum of all elements up to that index.
    >>> rolling_max([1, 2, 3, 2, 5])
    [1, 2, 3, 3, 5]
    >>> rolling_max([])
    []
    """
    result: List[int] = []
    running_max = None
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)
        result.append(running_max)
    return result


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_9_code import rolling_max

class TestRollingMax(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_single_element(self):
        self.assertEqual(rolling_max([1]), [1])

    def test_multiple_elements(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 5]), [1, 2, 3, 3, 5])

    def test_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3, -2, -5]), [-1, -1, -1, -1, -1])

    def test_mixed_numbers(self):
        self.assertEqual(rolling_max([1, -2, 3, -2, 5]), [1, 1, 3, 3, 5])

if __name__ == '__main__':
    unittest.main()


This script includes tests for empty list, single element, multiple elements, negative numbers, and mixed numbers. Each test checks if the output of the `rolling_max` function matches the expected result.