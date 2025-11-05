Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_52_code import below_threshold
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for e in l:
        if e >= t:
            return False
    return True

 Here is a unittest test script for the `below_threshold` function:


import unittest
from HumanEval_52_code import below_threshold

class TestBelowThreshold(unittest.TestCase):

    def test_below_threshold(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))
        self.assertTrue(below_threshold([0, 0, 0, 0], 1))
        self.assertFalse(below_threshold([100, 200, 300, 400], 10))
        self.assertTrue(below_threshold([], 10))
        self.assertTrue(below_threshold([-1, -2, -3, -4], 0))

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the `below_threshold` function, which tests the function with various inputs and verifies that the function returns the expected results. The test case is defined within the `TestBelowThreshold` class, and the test function is `test_below_threshold`.

The test script starts with the import statements, includes the function to be tested, and ends with the `unittest.main()` call to run the tests.