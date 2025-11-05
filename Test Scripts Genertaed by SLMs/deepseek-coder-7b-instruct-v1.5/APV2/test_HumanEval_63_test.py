You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_63_code import fibfib
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)


### Response:
Here is the unittest test suite for the provided Python function:


import unittest
from HumanEval_63_code import fibfib

class TestFibFib(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(fibfib(0), 0)

    def test_one(self):
        self.assertEqual(fibfib(1), 0)

    def test_two(self):
        self.assertEqual(fibfib(2), 1)

    def test_three(self):
        self.assertEqual(fibfib(3), 1)

    def test_four(self):
        self.assertEqual(fibfib(4), 2)

    def test_five(self):
        self.assertEqual(fibfib(5), 4)

    def test_six(self):
        self.assertEqual(fibfib(6), 6)

    def test_seven(self):
        self.assertEqual(fibfib(7), 10)

    def test_eight(self):
        self.assertEqual(fibfib(8), 24)

    def test_nine(self):
        self.assertEqual(fibfib(9), 44)

    def test_ten(self):
        self.assertEqual(fibfib(10), 88)

if __name__ == '__main__':
    unittest.main()


This test suite includes a series of tests that check the output of the `fibfib` function for a range of input values. The tests cover a small number of cases to ensure that the function is working correctly, but they could be extended to include more test cases if necessary.

Please note that this test suite assumes that the `fibfib` function is implemented correctly and that it follows the rules specified in the docstring. If the function does not behave as expected, the tests will fail, and you will need to correct the implementation of the function.