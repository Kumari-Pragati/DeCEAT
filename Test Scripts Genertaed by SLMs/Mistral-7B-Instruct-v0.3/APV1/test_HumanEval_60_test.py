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

 Here is a simple unittest test suite for the `sum_to_n` function:


import unittest
from HumanEval_60_code import sum_to_n

class TestSumToN(unittest.TestCase):
    def test_sum_to_n(self):
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(1), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes a single test case (`TestSumToN`) with a single test method (`test_sum_to_n`). The test method uses the `assertEqual` method provided by unittest to compare the expected output of the `sum_to_n` function with the actual output. If the outputs match, the test passes; otherwise, it fails.

You can run this test suite by saving it in a file (e.g., `test_sum_to_n.py`) and running the file using Python (`python test_sum_to_n.py`). The test suite will run all the tests and provide a summary of the results. If any tests fail, you will see an error message indicating which test failed and why.