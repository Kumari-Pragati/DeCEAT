system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Importing the function we want to test
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num(self):
        # Test cases covering different scenarios
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(14, 16), 16)
        self.assertEqual(choose_num(17, 18), -1)
        self.assertEqual(choose_num(19, 18), -1)

    def test_edge_cases(self):
        # Testing edge cases where x or y could be negative or zero
        self.assertEqual(choose_num(-1, 10), -1)
        self.assertEqual(choose_num(10, -1), -1)
        self.assertEqual(choose_num(0, 10), -1)
        self.assertEqual(choose_num(10, 0), -1)

if __name__ == '__main__':
    unittest.main()


This solution includes a `unittest` test suite that covers various scenarios as described in the problem statement. It tests both typical inputs and edge cases to ensure the function behaves correctly under different conditions.