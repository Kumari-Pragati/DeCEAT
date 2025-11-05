user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_13_code import greatest_common_divisor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return aassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_13_code import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_greatest_common_divisor(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(12, 15), 3)
        self.assertEqual(greatest_common_divisor(48, 18), 6)
        self.assertEqual(greatest_common_divisor(100, 20), 20)
        self.assertEqual(greatest_common_divisor(10, 25), 5)
        self.assertEqual(greatest_common_divisor(7, 3), 1)
        self.assertEqual(greatest_common_divisor(9, 3), 3)
        self.assertEqual(greatest_common_divisor(15, 3), 3)
        self.assertEqual(greatest_common_divisor(0, 0), 0)
        self.assertEqual(greatest_common_divisor(0, 5), 5)
        self.assertEqual(greatest_common_divisor(5, 0), 5)
        self.assertEqual(greatest_common_divisor(5, 10), 5)
        self.assertEqual(greatest_common_divisor(10, 5), 5)
        self.assertEqual(greatest_common_divisor(10, 20), 10)
        self.assertEqual(greatest_common_divisor(20, 10), 10)
        self.assertEqual(greatest_common_divisor(20, 4), 4)
        self.assertEqual(greatest_common_divisor(4, 20), 4)
        self.assertEqual(greatest_common_divisor(4, 0), 4)
        self.assertEqual(greatest_common_divisor(0, 4), 4)

if __name__ == '__main__':
    unittest.main()


This script includes a variety of test cases to ensure the function is working correctly. It tests the function with different inputs, including edge cases like 0 and 0, 0 and 5, 5 and 0, and 5 and 10.