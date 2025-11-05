system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_2_code import truncate_number
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1.0assistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):

    def test_truncate_number(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)
        self.assertAlmostEqual(truncate_number(2.0), 0.0)
        self.assertAlmostEqual(truncate_number(1.0), 0.0)
        self.assertAlmostEqual(truncate_number(0.5), 0.5)
        self.assertAlmostEqual(truncate_number(0.0), 0.0)
        self.assertAlmostEqual(truncate_number(1.5), 0.5)
        self.assertAlmostEqual(truncate_number(2.5), 0.5)
        self.assertAlmostEqual(truncate_number(3.0), 0.0)
        self.assertAlmostEqual(truncate_number(4.5), 0.5)
        self.assertAlmostEqual(truncate_number(5.0), 0.0)
        self.assertAlmostEqual(truncate_number(6.5), 0.5)
        self.assertAlmostEqual(truncate_number(7.0), 0.0)
        self.assertAlmostEqual(truncate_number(8.5), 0.5)
        self.assertAlmostEqual(truncate_number(9.0), 0.0)
        self.assertAlmostEqual(truncate_number(10.5), 0.5)
        self.assertAlmostEqual(truncate_number(11.0), 0.0)
        self.assertAlmostEqual(truncate_number(12.5), 0.5)
        self.assertAlmostEqual(truncate_number(13.0), 0.0)
        self.assertAlmostEqual(truncate_number(14.5), 0.5)
        self.assertAlmostEqual(truncate_number(15.0), 0.0)
        self.assertAlmostEqual(truncate_number(16.5), 0.5)
        self.assertAlmostEqual(truncate_number(17.0), 0.0)
        self.assertAlmostEqual(truncate_number(18.5), 0.5)
        self.assertAlmostEqual(truncate_number(19.0), 0.0)
        self.assertAlmostEqual(truncate_number(20.5), 0.5)
        self.assertAlmostEqual(truncate_number(21.0), 0.0)
        self.assertAlmostEqual(truncate_number(22.5), 0.5)
        self.assertAlmostEqual(truncate_number(23.0), 0.0)
        self.assertAlmostEqual(truncate_number(24.5), 0.5)
        self.assertAlmostEqual(truncate_number(25.0), 0.0)
        self.assertAlmostEqual(truncate_number(26.5), 0.5)
        self.assertAlmostEqual(truncate_number(27.0), 0.0)
        self.assertAlmostEqual(truncate_number(28.5), 0.5)
        self.assertAlmostEqual(truncate_number(29.0), 0.0)
        self.assertAlmostEqual(truncate_number(30.5), 0.5)
        self.assertAlmostEqual(truncate_number(31.0), 0.0)
        self.assertAlmostEqual(truncate_number(32.5), 0.5)
        self.assertAlmostEqual(truncate_number(33.0), 0.0)
        self.assertAlmostEqual(truncate_number(34.5), 0.5)
        self.assertAlmostEqual(truncate_number(35.0), 0.0)
        self.assertAlmostEqual(truncate_number(36.5), 0.5)
        self.assertAlmostEqual(truncate_number(37.0), 0.0)
        self.assertAlmostEqual(truncate_number(38.5), 0.5)
        self.assertAlmostEqual(truncate_number(39.0), 0.0)
        self.assertAlmostEqual(truncate_number(40.5), 0.5)
        self.assertAlmostEqual(truncate_number(41.0), 0.0)
        self.assertAlmostEqual(truncate_number(42.5), 0.5)
        self.assertAlmostEqual(truncate_number(43.0), 0.0)
        self.assertAlmostEqual(truncate_number(44.5), 0.5)
        self.assertAlmostEqual(truncate_number(45.0), 0.0)
        self.assertAlmostEqual(truncate_number(46.5), 0.5)
        self.assertAlmostEqual(truncate_number(47.0), 0.0)
        self.assertAlmostEqual(truncate_number(48.5), 0.5)
        self.assertAlmostEqual(truncate_number(49.0), 0.0)
        self.assertAlmostEqual(truncate_number(50.5), 0.5)
        self.assertAlmostEqual(truncate_number(51.0), 0.0)
        self.assertAlmostEqual(truncate_number(52.5), 0.5)
        self.assertAlmostEqual(truncate_number(53.0), 0.0)
        self.assertAlmostEqual(truncate_number(54.5), 0.5)
        self.assertAlmostEqual(truncate_number(55.0), 0.0)
        self.assertAlmostEqual(truncate_number(56.5), 0.5)
        self.assertAlmostEqual