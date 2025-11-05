Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `sum_to_n` function:


import unittest
from HumanEval_60_code import sum_to_n

class TestSumToN(unittest.TestCase):
    def test_sum_to_n(self):
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(1), 1)
        self.assertEqual(sum_to_n(0), 0)
        self.assertEqual(sum_to_n(-1), 0)
        self.assertEqual(sum_to_n(float('inf')), float('inf'))

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the `TestSumToN` class that tests the `sum_to_n` function with various inputs, including negative numbers, floating-point numbers, and special cases like 0 and infinity. The test case uses the `assertEqual` method to verify that the output of the `sum_to_n` function matches the expected output for each test case. The test script ends with the standard boilerplate for running unittest tests.