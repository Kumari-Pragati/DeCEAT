You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_49_code import modp

class TestModPFunction(unittest.TestCase):

    def test_modp_with_positive_integers(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

    def test_modp_with_negative_integers(self):
        self.assertEqual(modp(-3, 5), 3)
        self.assertEqual(modp(-1101, 101), 2)
        self.assertEqual(modp(-0, 101), 1)
        self.assertEqual(modp(-3, 11), 8)
        self.assertEqual(modp(-100, 101), 1)

    def test_modp_with_zero(self):
        self.assertEqual(modp(0, 5), 1)
        self.assertEqual(modp(0, 101), 1)

    def test_modp_with_large_numbers(self):
        self.assertEqual(modp(1000, 100000007), 128)
        self.assertEqual(modp(2000, 100000007), 1048576)

    def test_modp_with_edge_cases(self):
        self.assertEqual(modp(1, 2), 1)
        self.assertEqual(modp(2, 2), 0)
        self.assertEqual(modp(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000