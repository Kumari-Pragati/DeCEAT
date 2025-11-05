You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_77_code import iscube
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
        iscube(1) ==> True
        iscube(2) ==> False
        iscube(-1) ==> True
        iscube(64) ==> True
        iscube(0) ==> True
        iscube(180) ==> False
    '''

    a = abs(a)
    return int(round(a ** (1.0 / 3))) ** 3 == a

 Here is a complete unittest test suite for the `iscube` function:


import unittest
from HumanEval_77_code import iscube

class TestIsCube(unittest.TestCase):

    def test_iscube_positive_numbers(self):
        self.assertTrue(iscube(1))
        self.assertFalse(iscube(2))
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(0))

    def test_iscube_negative_numbers(self):
        self.assertTrue(iscube(-1))
        self.assertFalse(iscube(-2))
        self.assertFalse(iscube(-64))
        self.assertFalse(iscube(-0))

    def test_iscube_zero(self):
        self.assertTrue(iscube(0))

    def test_iscube_large_numbers(self):
        self.assertTrue(iscube(27))
        self.assertFalse(iscube(180))
        self.assertTrue(iscube(216))
        self.assertFalse(iscube(256))

    def test_iscube_small_numbers(self):
        self.assertTrue(iscube(1))
        self.assertFalse(iscube(0))
        self.assertFalse(iscube(-1))

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases for positive, negative, zero, large, and small numbers to ensure the `iscube` function works correctly for various inputs.