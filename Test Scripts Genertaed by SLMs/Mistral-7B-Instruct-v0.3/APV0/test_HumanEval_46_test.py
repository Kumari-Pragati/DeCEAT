Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_46_code import fib4
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence. Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]

 Here is a unittest test script for the `fib4` function:


import unittest
from HumanEval_46_code import fib4

class TestFib4(unittest.TestCase):
    def test_fib4(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)
        self.assertEqual(fib4(4), 2)
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)
        self.assertEqual(fib4(8), 26)
        self.assertEqual(fib4(9), 48)
        self.assertEqual(fib4(10), 88)
        self.assertEqual(fib4(15), 317)
        self.assertEqual(fib4(20), 676)
        self.assertEqual(fib4(30), 20040)
        self.assertEqual(fib4(40), 514228)
        self.assertEqual(fib4(50), 12586269)
        self.assertEqual(fib4(60), 304541065)
        self.assertEqual(fib4(70), 757078368)
        self.assertEqual(fib4(80), 1927972585)
        self.assertEqual(fib4(90), 4836797440)
        self.assertEqual(fib4(100), 12139322442)

if __name__ == '__main__':
    unittest.main()


This test script includes a `TestFib4` class that contains a `test_fib4` method. This method tests the `fib4` function with various inputs and asserts that the function returns the expected output. The test script then calls `unittest.main()` to run the tests.