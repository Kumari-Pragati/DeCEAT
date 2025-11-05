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
    return int(round(a ** (1.0 / 3))) ** 3 == a

 Here is a unittest test script for the `iscube` function:


import unittest
from HumanEval_77_code import iscube

class TestIsCube(unittest.TestCase):
    def test_iscube(self):
        self.assertTrue(iscube(1))
        self.assertFalse(iscube(2))
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(0))
        self.assertFalse(iscube(180))
        self.assertTrue(iscube(8))
        self.assertTrue(iscube(27))
        self.assertFalse(iscube(125))  # a perfect cube but with a negative sign
        self.assertTrue(iscube(-27))  # the same cube but with a negative sign
        self.assertFalse(iscube(126))  # not a cube
        self.assertFalse(iscube(-126))  # not a cube

if __name__ == '__main__':
    unittest.main()


This test script includes a `TestIsCube` class that inherits from `unittest.TestCase`. Inside this class, there is a method `test_iscube` that tests the `iscube` function with various examples.

The test cases cover positive and negative integers, perfect cubes, and non-cubes. The `assertTrue` and `assertFalse` methods are used to verify the expected output for each test case.

When you run this script, it will execute the tests and print the results. If all tests pass, the function is working correctly. If any tests fail, you will see an error message indicating which test failed and the expected and actual outputs.