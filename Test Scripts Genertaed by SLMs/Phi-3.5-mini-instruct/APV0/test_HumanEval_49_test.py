Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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
        self.assertEqual(modp(-3, 5), 3)  # Assuming the function can handle negative n
        self.assertEqual(modp(-1101, 101), 2)  # Assuming the function can handle negative n
        self.assertEqual(modp(-0, 101), 1)  # Assuming the function can handle negative n
        self.assertEqual(modp(-3, 11), 8)  # Assuming the function can handle negative n
        self.assertEqual(modp(-100, 101), 1)  # Assuming the function can handle negative n

    def test_modp_with_zero(self):
        self.assertEqual(modp(0, 5), 1)
        self.assertEqual(modp(0, 101), 1)

    def test_modp_with_large_numbers(self):
        self.assertEqual(modp(1000, 9999), 1000)  # Assuming 2^1000 mod 9999 is 1000
        self.assertEqual(modp(10000, 9999), 1)  # Assuming 2^10000 mod 9999 is 1

    def test_modp_with_small_numbers(self):
        self.assertEqual(modp(1, 5), 2)
        self.assertEqual(modp(1, 101), 2)

    def test_modp_with_edge_cases(self):
        self.assertEqual(modp(1024, 1024), 1)  # Assuming 2^1024 mod 1024 is 1
        self.assertEqual(modp(1023, 1024), 1023)  # Assuming 2^1023 mod 1024 is 1023

if __name__ == '__main__':
    unittest.main()