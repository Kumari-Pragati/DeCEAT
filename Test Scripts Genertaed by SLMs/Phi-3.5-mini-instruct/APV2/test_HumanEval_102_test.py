You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num_with_even_numbers(self):
        self.assertEqual(choose_num(12, 14), 14)
        self.assertEqual(choose_num(10, 12), 12)
        self.assertEqual(choose_num(8, 10), 10)

    def test_choose_num_with_odd_numbers(self):
        self.assertEqual(choose_num(11, 13), -1)
        self.assertEqual(choose_num(9, 11), -1)
        self.assertEqual(choose_num(7, 9), -1)

    def test_choose_num_with_equal_numbers(self):
        self.assertEqual(choose_num(12, 12), -1)
        self.assertEqual(choose_num(10, 10), -1)
        self.assertEqual(choose_num(8, 8), -1)

    def test_choose_num_with_x_greater_than_y(self):
        self.assertEqual(choose_num(15, 12), -1)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(11, 10), -1)

    def test_choose_num_with_y_greater_than_x_and_even(self):
        self.assertEqual(choose_num(10, 14), 14)
        self.assertEqual(choose_num(8, 14), 14)
        self.assertEqual(choose_num(6, 14), 14)

    def test_choose_num_with_y_greater_than_x_and_odd(self):
        self.assertEqual(choose_num(11, 13), -1)
        self.assertEqual(choose_num(9, 13), -1)
        self.assertEqual(choose_num(7, 13), -1)

if __name__ == '__main__':
    unittest.main()