user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_63_code import fibfib

class TestFibFib(unittest.TestCase):

    def test_fibfib(self):
        self.assertEqual(fibfib(0), 0)
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(2), 1)
        self.assertEqual(fibfib(3), 2)
        self.assertEqual(fibfib(4), 3)
        self.assertEqual(fibfib(5), 4)
        self.assertEqual(fibfib(6), 9)
        self.assertEqual(fibfib(7), 13)
        self.assertEqual(fibfib(8), 24)
        self.assertEqual(fibfib(9), 43)
        self.assertEqual(fibfib(10), 77)

if __name__ == '__main__':
    unittest.main()


This script tests the `fibfib` function with various inputs and checks if the output matches the expected result. The `assertEqual` method is used to compare the output of the function with the expected result. If the output does not match the expected result, the test will fail and an error message will be displayed.