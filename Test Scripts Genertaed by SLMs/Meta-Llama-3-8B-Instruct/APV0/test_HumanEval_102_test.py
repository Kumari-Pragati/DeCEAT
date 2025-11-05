user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_102_code import choose_num
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1assistant

Here is a unittest test script for the `choose_num` function:

Python
import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num_positive_numbers(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(14, 14), -1)
        self.assertEqual(choose_num(10, 20), 20)
        self.assertEqual(choose_num(20, 10), -1)

    def test_choose_num_negative_numbers(self):
        with self.assertRaises(ValueError):
            choose_num(-1, 1)
        with self.assertRaises(ValueError):
            choose_num(1, -1)

    def test_choose_num_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            choose_num(12.5, 15)
        with self.assertRaises(TypeError):
            choose_num(13, 12.5)

if __name__ == '__main__':
    unittest.main()


This script includes three test cases:

1. `test_choose_num_positive_numbers`: This test case checks the function with positive numbers. It tests the function with different inputs, including cases where the function returns -1.

2. `test_choose_num_negative_numbers`: This test case checks the function with negative numbers. It tests the function with negative numbers and checks if it raises a ValueError.

3. `test_choose_num_non_integer_numbers`: This test case checks the function with non-integer numbers. It tests the function with float numbers and checks if it raises a TypeError.

The `unittest.main()` function is used to run the test cases.