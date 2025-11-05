user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 *... * i).
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
    return retassistant

Here is a unittest test script for the function `f`:

import unittest
from HumanEval_106_code import f

class TestF(unittest.TestCase):
    def test_f(self):
        # Test cases
        self.assertEqual(f(1), [1])
        self.assertEqual(f(2), [1, 2])
        self.assertEqual(f(3), [1, 2, 3])
        self.assertEqual(f(4), [1, 2, 6, 24])
        self.assertEqual(f(5), [1, 2, 6, 24, 15])
        self.assertEqual(f(6), [1, 2, 6, 24, 30, 90])
        self.assertEqual(f(7), [1, 2, 6, 24, 30, 90, 120])
        self.assertEqual(f(8), [1, 2, 6, 24, 30, 90, 120, 720])
        self.assertEqual(f(9), [1, 2, 6, 24, 30, 90, 120, 720, 362880])

    def test_f_edge_cases(self):
        # Test edge cases
        self.assertEqual(f(0), [])
        self.assertEqual(f(-1), [])

    def test_f_invalid_input(self):
        # Test invalid input
        with self.assertRaises(TypeError):
            f("hello")

if __name__ == '__main__':
    unittest.main()

This script includes three test functions:

1. `test_f`: This function tests the function `f` with various input values, including small numbers, large numbers, and edge cases.
2. `test_f_edge_cases`: This function tests the function `f` with edge cases, such as input values of 0 and -1.
3. `test_f_invalid_input`: This function tests the function `f` with invalid input, such as a string.

The script uses the `assertEqual` method to check if the output of the function `f` matches the expected output. The `assertRaises` method is used to check if the function raises a `TypeError` when given invalid input.

You can run this script directly to execute the tests.