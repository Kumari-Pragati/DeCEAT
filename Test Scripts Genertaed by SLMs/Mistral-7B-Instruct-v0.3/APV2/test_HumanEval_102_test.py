You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return y - 1

 Here is the complete unittest test suite for the `choose_num` function:


import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num_valid_even(self):
        self.assertEqual(choose_num(12, 14), 14)
        self.assertEqual(choose_num(10, 18), 18)
        self.assertEqual(choose_num(2, 4), 4)
        self.assertEqual(choose_num(6, 6), -1)

    def test_choose_num_valid_odd(self):
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(15, 13), -1)
        self.assertEqual(choose_num(1, 3), -1)

    def test_choose_num_invalid_input(self):
        self.assertEqual(choose_num(-5, 10), -1)
        self.assertEqual(choose_num(10, -5), -1)
        self.assertEqual(choose_num(0, 10), -1)
        self.assertEqual(choose_num(10, 0), -1)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_choose_num_valid_even` checks the function's behavior when both numbers are even and greater than each other.
2. `test_choose_num_valid_odd` checks the function's behavior when both numbers are odd or one number is odd and the other is even but greater than the odd number.
3. `test_choose_num_invalid_input` checks the function's behavior when the input is invalid (negative numbers, zero, or one number is less than the other).

Each test case uses the `assertEqual` method to compare the expected output with the actual output of the `choose_num` function.