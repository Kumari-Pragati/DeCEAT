You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_106_code import f
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """

    ret = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            x = 1
            for j in range(1, i + 1):
                x *= j
            ret += [x]
        else:
            x = 0
            for j in range(1, i + 1):
                x += j
            ret += [x]
    return ret

 Here is the complete unittest test suite for the provided Python function `f(n)`. I've created test cases for both even and odd `n` values.


import unittest
from HumanEval_106_code import f

class TestFunctionF(unittest.TestCase):

    def test_f_even(self):
        self.assertEqual(f(2), [1])
        self.assertEqual(f(4), [1, 2, 6])
        self.assertEqual(f(6), [1, 2, 6, 24])
        self.assertEqual(f(8), [1, 2, 6, 24, 120])

    def test_f_odd(self):
        self.assertEqual(f(1), [1])
        self.assertEqual(f(3), [1, 2, 3])
        self.assertEqual(f(5), [1, 2, 6, 15])
        self.assertEqual(f(7), [1, 2, 6, 15, 22])

if __name__ == '__main__':
    unittest.main()


This test suite includes two test functions: `test_f_even` and `test_f_odd`. Each test function checks the correctness of the function `f` for a specific set of even and odd input values. The test suite runs the tests and compares the expected output with the actual output.