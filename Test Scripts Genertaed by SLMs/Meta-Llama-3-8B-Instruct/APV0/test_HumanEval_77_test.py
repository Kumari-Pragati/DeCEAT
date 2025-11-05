user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return int(round(a ** (1.0 / 3))) ** 3 == aassistant

Here is the unittest test script for the `iscube` function:

import unittest
from HumanEval_77_code import iscube

class TestIsCube(unittest.TestCase):
    def test_positive_cubes(self):
        self.assertTrue(iscube(1))
        self.assertTrue(iscube(27))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(125))
        self.assertTrue(iscube(216))

    def test_negative_cubes(self):
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(-27))
        self.assertTrue(iscube(-64))
        self.assertTrue(iscube(-125))
        self.assertTrue(iscube(-216))

    def test_non_cubes(self):
        self.assertFalse(iscube(2))
        self.assertFalse(iscube(3))
        self.assertFalse(iscube(4))
        self.assertFalse(iscube(5))
        self.assertFalse(iscube(6))

    def test_edge_cases(self):
        self.assertTrue(iscube(0))
        self.assertFalse(iscube(1.5))  # not an integer

if __name__ == '__main__':
    unittest.main()

This script defines a test class `TestIsCube` with four test methods:

1. `test_positive_cubes`: Tests the function with positive cube numbers.
2. `test_negative_cubes`: Tests the function with negative cube numbers.
3. `test_non_cubes`: Tests the function with numbers that are not cubes.
4. `test_edge_cases`: Tests the function with edge cases, such as 0 and non-integer values.

Each test method uses the `assertTrue` and `assertFalse` methods to verify that the `iscube` function returns the expected results.