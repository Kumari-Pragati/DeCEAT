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
    return a

 Here is a unittest test script for the `greatest_common_divisor` function:


import unittest
from HumanEval_13_code import greatest_common_divisor

class TestGCD(unittest.TestCase):

    def test_greatest_common_divisor(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(48, 18), 6)
        self.assertEqual(greatest_common_divisor(12, 36), 12)
        self.assertEqual(greatest_common_divisor(100, 250), 25)
        self.assertEqual(greatest_common_divisor(1, 1), 1)
        self.assertEqual(greatest_common_divisor(0, 1), 1)
        self.assertEqual(greatest_common_divisor(0, 0), 0)
        self.assertEqual(greatest_common_divisor(-3, 5), 1)
        self.assertEqual(greatest_common_divisor(-25, 15), 5)
        self.assertEqual(greatest_common_divisor(-25, -15), 5)

if __name__ == '__main__':
    unittest.main()


This test script includes a `TestGCD` class that contains a method `test_greatest_common_divisor`. This method contains several assertions that test the `greatest_common_divisor` function with various inputs. The test script starts with `import unittest` and includes `from HumanEval_13_code import greatest_common_divisor`. It ends with `if __name__ == '__main__': unittest.main()`.