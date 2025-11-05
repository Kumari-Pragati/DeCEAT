You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a simple unittest test suite for the given Python function `iscube`. The test cases cover a range of positive and negative integers, including zero, and a non-cube number.


import unittest
from HumanEval_77_code import iscube

class TestIsCube(unittest.TestCase):

    def test_iscube_positive_numbers(self):
        self.assertTrue(iscube(1))
        self.assertTrue(iscube(8))
        self.assertTrue(iscube(27))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(125))
        self.assertTrue(iscube(216))

    def test_iscube_zero(self):
        self.assertTrue(iscube(0))

    def test_iscube_negative_numbers(self):
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(-8))
        self.assertTrue(iscube(-27))
        self.assertTrue(iscube(-64))
        self.assertTrue(iscube(-125))
        self.assertTrue(iscube(-216))

    def test_iscube_non_cube_number(self):
        self.assertFalse(iscube(180))

if __name__ == '__main__':
    unittest.main()


This test suite includes three test methods:

1. `test_iscube_positive_numbers`: Tests the function with positive integers.
2. `test_iscube_zero`: Tests the function with zero.
3. `test_iscube_negative_numbers`: Tests the function with negative integers.
4. `test_iscube_non_cube_number`: Tests the function with a non-cube number.

Each test method checks the function's behavior for a specific set of inputs and verifies the expected output using the `assertTrue` and `assertFalse` methods provided by the `unittest.TestCase` class.