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
    return y - 1

 Here is a comprehensive unittest test suite for the `choose_num` function:


import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num_valid_even_numbers(self):
        self.assertEqual(choose_num(2, 4), 4)
        self.assertEqual(choose_num(6, 8), 8)
        self.assertEqual(choose_num(10, 14), 14)
        self.assertEqual(choose_num(18, 20), 20)

    def test_choose_num_valid_odd_numbers(self):
        self.assertEqual(choose_num(1, 4), -1)
        self.assertEqual(choose_num(3, 6), -1)
        self.assertEqual(choose_num(5, 10), -1)
        self.assertEqual(choose_num(17, 18), -1)

    def test_choose_num_equal_numbers(self):
        self.assertEqual(choose_num(2, 2), -1)
        self.assertEqual(choose_num(4, 4), -1)
        self.assertEqual(choose_num(6, 6), -1)
        self.assertEqual(choose_num(8, 8), -1)

    def test_choose_num_invalid_arguments(self):
        self.assertEqual(choose_num(-1, 1), -1)
        self.assertEqual(choose_num(1, 0), -1)
        self.assertEqual(choose_num(1, -1), -1)
        self.assertEqual(choose_num(0, 1), -1)
        self.assertEqual(choose_num(1, 1), -1)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for valid even numbers, valid odd numbers, equal numbers, and invalid arguments. It covers a wide range of test cases to ensure the `choose_num` function works correctly.