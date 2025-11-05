system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the given Python function:

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
        self.assertEqual(greatest_common_divisor(24, 30), 6)
        self.assertEqual(greatest_common_divisor(36, 12), 12)
        self.assertEqual(greatest_common_divisor(9, 3), 3)
        self.assertEqual(greatest_common_divisor(15, 5), 5)
        self.assertEqual(greatest_common_divisor(20, 4), 4)

    def test_greatest_common_divisor_edge_cases(self):
        self.assertEqual(greatest_common_divisor(0, 0), 0)
        self.assertEqual(greatest_common_divisor(0, 1), 1)
        self.assertEqual(greatest_common_divisor(1, 0), 1)
        self.assertEqual(greatest_common_divisor(0, 2), 2)
        self.assertEqual(greatest_common_divisor(2, 0), 2)

if __name__ == '__main__':
    unittest.main()