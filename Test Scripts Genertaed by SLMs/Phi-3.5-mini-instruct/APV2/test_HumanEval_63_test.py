You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 import unittest
from HumanEval_63_code import fibfib

class TestFibFib(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(fibfib(0), 0)
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(2), 1)

    def test_known_values(self):
        self.assertEqual(fibfib(5), 4)
        self.assertEqual(fibfib(8), 24)

    def test_edge_cases(self):
        self.assertEqual(fibfib(3), 1)
        self.assertEqual(fibfib(4), 2)
        self.assertEqual(fibfib(6), 10)

    def test_large_value(self):
        # Testing with a larger value to ensure efficiency
        # Note: This test may take a while to run due to the function's complexity
        self.assertEqual(fibfib(10), 124)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            fibfib('a')
        with self.assertRaises(TypeError):
            fibfib(None)

if __name__ == '__main__':
    unittest.main()