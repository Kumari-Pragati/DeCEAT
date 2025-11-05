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

 import unittest
from HumanEval_77_code import iscube

class TestIsCube(unittest.TestCase):

    def test_positive_integers(self):
        self.assertTrue(iscube(1))
        self.assertFalse(iscube(2))
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(0))

    def test_negative_integers(self):
        self.assertTrue(iscube(-1))
        self.assertFalse(iscube(-8))
        self.assertTrue(iscube(-64))

    def test_zero(self):
        self.assertTrue(iscube(0))

    def test_non_cube_integers(self):
        self.assertFalse(iscube(180))
        self.assertFalse(iscube(27))  # This should be False, but it's a test case to ensure the function handles non-cubes correctly.

    def test_edge_cases(self):
        self.assertTrue(iscube(-8))
        self.assertTrue(iscube(8))

if __name__ == '__main__':
    unittest.main()