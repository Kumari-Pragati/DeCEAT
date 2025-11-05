You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 import unittest
from HumanEval_106_code import f

class TestF(unittest.TestCase):

    def test_f_even_index(self):
        self.assertEqual(f(2), [1, 2])

    def test_f_odd_index(self):
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

    def test_f_zero(self):
        self.assertEqual(f(0), [])

    def test_f_negative(self):
        self.assertEqual(f(-1), [])

    def test_f_large_number(self):
        self.assertEqual(f(10), [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800])

    def test_f_large_number_with_odd_index(self):
        self.assertEqual(f(11), [1, 2, 6, 24, 15, 15, 105, 945, 9450, 103950, 133450])

if __name__ == '__main__':
    unittest.main()