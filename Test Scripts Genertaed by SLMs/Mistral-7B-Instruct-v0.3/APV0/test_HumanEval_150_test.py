Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_150_code import x_or_y
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x

 Here is a unittest test script for the `x_or_y` function:


import unittest
from HumanEval_150_code import x_or_y

class TestXOrY(unittest.TestCase):

    def test_x_or_y(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)
        self.assertEqual(x_or_y(15, 8, 5), 5)
        self.assertEqual(x_or_y(2, 1, 2), 1)
        self.assertEqual(x_or_y(4, 2, 4), 2)
        self.assertEqual(x_or_y(19, 19, 19), 19)
        self.assertEqual(x_or_y(1, 1, 2), 2)
        self.assertEqual(x_or_y(0, 0, 1), 1)
        self.assertEqual(x_or_y(-1, -1, 1), 1)
        self.assertEqual(x_or_y(29, 29, 29), 29)

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the `x_or_y` function with various inputs. The test case uses the `assertEqual` method to check if the function returns the expected output for each test case.