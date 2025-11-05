You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_49_code import modp
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret

 Here is the complete unittest test suite for the `modp` function:


import unittest
from HumanEval_49_code import modp

class TestModP(unittest.TestCase):

    def test_modp_3_5(self):
        self.assertEqual(modp(3, 5), 3)

    def test_modp_1101_101(self):
        self.assertEqual(modp(1101, 101), 2)

    def test_modp_0_101(self):
        self.assertEqual(modp(0, 101), 1)

    def test_modp_3_11(self):
        self.assertEqual(modp(3, 11), 8)

    def test_modp_100_101(self):
        self.assertEqual(modp(100, 101), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes five test cases for the `modp` function, covering various edge cases and different input combinations. The test cases are named descriptively to make it easy to understand what each test is testing.