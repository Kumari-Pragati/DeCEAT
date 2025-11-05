Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_53_code import add
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

 Here is a simple unittest test script for the given function. I've added some test cases to cover different scenarios, including negative numbers, zero, and large numbers.


import unittest
from HumanEval_53_code import add

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-5, -7), -12)

    def test_add_zero(self):
        self.assertEqual(add(0, 3), 3)
        self.assertEqual(add(-3, 0), -3)
        self.assertEqual(add(0, 0), 0)

    def test_large_numbers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)
        self.assertEqual(add(-1000000, -2000000), -3000000)

if __name__ == '__main__':
    unittest.main()


This test script includes four test cases:

1. `test_add_positive_numbers`: Tests the function with positive numbers.
2. `test_add_negative_numbers`: Tests the function with negative numbers.
3. `test_add_zero`: Tests the function with zero.
4. `test_large_numbers`: Tests the function with large numbers.

You can run this script directly by saving it as a .py file and running it from the command line using `python filename.py`. If the function passes all the tests, the test script will print "...ok" for each test case, indicating that the function is working correctly. If any test fails, the test script will print an error message explaining the failure.