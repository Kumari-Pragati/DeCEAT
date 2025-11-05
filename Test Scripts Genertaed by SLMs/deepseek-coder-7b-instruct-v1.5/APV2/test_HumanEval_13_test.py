You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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
    return a


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_13_code import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(36, 48), 12)
        self.assertEqual(greatest_common_divisor(101, 103), 1)

    def test_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-25, -15), 5)
        self.assertEqual(greatest_common_divisor(-36, 48), 12)
        self.assertEqual(greatest_common_divisor(-101, -103), 1)

    def test_mixed_numbers(self):
        self.assertEqual(greatest_common_divisor(-25, 15), 5)
        self.assertEqual(greatest_common_divisor(36, -48), 12)
        self.assertEqual(greatest_common_divisor(-101, 103), 1)

    def test_zero(self):
        self.assertEqual(greatest_common_divisor(0, 15), 15)
        self.assertEqual(greatest_common_divisor(36, 0), 36)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            greatest_common_divisor(15, 'a')
        with self.assertRaises(TypeError):
            greatest_common_divisor('a', 15)
        with self.assertRaises(TypeError):
            greatest_common_divisor('a', 'b')

if __name__ == '__main__':
    unittest.main()


This suite includes tests for positive numbers, negative numbers, mixed numbers, zero, and invalid input. It checks if the function returns the expected greatest common divisor for each case.