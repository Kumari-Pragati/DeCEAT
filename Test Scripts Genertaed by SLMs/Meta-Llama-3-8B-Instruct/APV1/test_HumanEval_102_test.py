user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(10, 10), -1)
        self.assertEqual(choose_num(14, 16), 14)
        self.assertEqual(choose_num(15, 16), 14)

    def test_x_greater_than_y(self):
        self.assertEqual(choose_num(15, 12), -1)
        self.assertEqual(choose_num(16, 15), -1)
        self.assertEqual(choose_num(17, 16), -1)

    def test_y_is_even(self):
        self.assertEqual(choose_num(12, 14), 14)
        self.assertEqual(choose_num(10, 12), 12)
        self.assertEqual(choose_num(14, 16), 14)

    def test_x_and_y_are_equal(self):
        self.assertEqual(choose_num(10, 10), -1)
        self.assertEqual(choose_num(12, 12), -1)
        self.assertEqual(choose_num(14, 14), -1)

    def test_y_is_not_even(self):
        self.assertEqual(choose_num(12, 13), 12)
        self.assertEqual(choose_num(10, 11), 10)
        self.assertEqual(choose_num(14, 15), 14)

if __name__ == '__main__':
    unittest.main()


This test suite covers all the possible scenarios and edge cases for the given function. It includes tests for positive numbers, x greater than y, y being even, x and y being equal, and y not being even.