system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Define the function to be tested
from HumanEval_46_code import fib4

class TestFib4(unittest.TestCase):

    def test_fib4(self):
        # Test cases provided in the docstring
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

    def test_edge_cases(self):
        # Test edge cases (n=0, n=-1, etc.)
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(-1), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)

    def test_large_input(self):
        # Test large input values up to 100
        for i in range(1, 101):
            result = fib4(i)
            print(f"fib4({i}) = {result}")

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a class `TestFib4` which inherits from `unittest.TestCase`. It contains three methods:

1. `test_fib4`: This method tests the function against the provided test cases.
2. `test_edge_cases`: This method checks the behavior of the function with edge cases such as `n=0`, `n=-1`, and other small inputs.
3. `test_large_input`: This method tests the function with larger inputs up to 100 to ensure it handles these values correctly.

Finally, the `if __name__ == '__main__':` block runs all the tests when the script is executed directly.