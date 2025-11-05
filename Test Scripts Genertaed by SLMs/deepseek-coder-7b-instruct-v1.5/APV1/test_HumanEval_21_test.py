You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):

    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
        self.assertEqual(rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
        self.assertEqual(rescale_to_unit([100.0, 200.0, 300.0, 400.0, 500.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
        self.assertEqual(rescale_to_unit([0.0, 0.0, 0.0, 0.0, 0.0]), [0.0, 0.0, 0.0, 0.0, 0.0])
        self.assertEqual(rescale_to_unit([1.0, 1.0, 1.0, 1.0, 1.0]), [0.0, 0.0, 0.0, 0.0, 0.0])
        self.assertEqual(rescale_to_unit([-1.0, -2.0, -3.0, -4.0, -5.0]), [1.0, 1.25, 1.5, 1.75, 2.0])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure that the function is working correctly. It tests with both positive and negative numbers, as well as with numbers that are all the same. It also tests with a list where the minimum and maximum values are the same, which should result in a list of all zeros.