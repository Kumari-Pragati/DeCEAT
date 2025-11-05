system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_60_code import sum_to_n
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum(range(n + 1))


assistant

import unittest

# Importing the function we want to test
from HumanEval_60_code import sum_to_n

class TestSumToN(unittest.TestCase):

    def test_sum_to_n(self):
        # Test cases provided in the docstring
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(1), 1)

    def test_edge_cases(self):
        # Edge case tests
        self.assertEqual(sum_to_n(-1), 0)  # Negative number should be zero
        self.assertEqual(sum_to_n(0), 0)   # Zero input should be zero
        self.assertEqual(sum_to_n(1000), 500500)  # Large number should work correctly

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestSumToN` class within a `unittest` module, which contains two methods: `test_sum_to_n` and `test_edge_cases`. The `test_sum_to_n` method includes assertions based on the provided examples in the docstring of the `sum_to_n` function. The `test_edge_cases` method includes additional edge cases such as negative numbers and large inputs to ensure robustness. Finally, if this script is run directly (not imported into another script), it will execute all defined tests using `unittest.main()`.