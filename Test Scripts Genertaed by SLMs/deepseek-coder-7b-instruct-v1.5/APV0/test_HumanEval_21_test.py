You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_21_code import rescale_to_unit
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
        self.assertEqual(rescale_to_unit([10.0, 20.0, 30.0]), [0.0, 0.5, 1.0])
        self.assertEqual(rescale_to_unit([100.0, 200.0]), [0.0, 1.0])
        self.assertEqual(rescale_to_unit([0.0, 0.0, 0.0]), [0.0, 0.0, 0.0])
        self.assertEqual(rescale_to_unit([1.0]), [0.0])

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestRescaleToUnit` that includes a test method `test_rescale_to_unit`. This method tests the `rescale_to_unit` function with different input lists and checks if the output matches the expected output.

The `unittest.main()` at the end makes this script runnable directly, executing all test methods in the `TestRescaleToUnit` class.

Please note that you need to have the `rescale_to_unit` function implemented in the `HumanEval_21_code` module for this script to work.