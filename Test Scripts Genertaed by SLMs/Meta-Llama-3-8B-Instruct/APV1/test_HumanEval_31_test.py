user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_31_code import is_prime
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return Trueassistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_31_code import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime_positive_numbers(self):
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13441))
        self.assertTrue(is_prime(61))

    def test_is_prime_negative_numbers(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-3))

    def test_is_prime_zero(self):
        self.assertFalse(is_prime(0))

    def test_is_prime_one(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_two(self):
        self.assertFalse(is_prime(2))

    def test_is_prime_four(self):
        self.assertFalse(is_prime(4))

    def test_is_prime_six(self):
        self.assertFalse(is_prime(6))

    def test_is_prime_prime_numbers(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(31))
        self.assertTrue(is_prime(37))
        self.assertTrue(is_prime(41))
        self.assertTrue(is_prime(43))
        self.assertTrue(is_prime(47))
        self.assertTrue(is_prime(53))
        self.assertTrue(is_prime(59))
        self.assertTrue(is_prime(61))
        self.assertTrue(is_prime(67))
        self.assertTrue(is_prime(71))
        self.assertTrue(is_prime(73))
        self.assertTrue(is_prime(79))
        self.assertTrue(is_prime(83))
        self.assertTrue(is_prime(89))
        self.assertTrue(is_prime(97))
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(103))
        self.assertTrue(is_prime(107))
        self.assertTrue(is_prime(109))
        self.assertTrue(is_prime(113))
        self.assertTrue(is_prime(127))
        self.assertTrue(is_prime(131))
        self.assertTrue(is_prime(137))
        self.assertTrue(is_prime(139))
        self.assertTrue(is_prime(149))
        self.assertTrue(is_prime(151))
        self.assertTrue(is_prime(157))
        self.assertTrue(is_prime(163))
        self.assertTrue(is_prime(167))
        self.assertTrue(is_prime(173))
        self.assertTrue(is_prime(179))
        self.assertTrue(is_prime(181))
        self.assertTrue(is_prime(191))
        self.assertTrue(is_prime(193))
        self.assertTrue(is_prime(197))
        self.assertTrue(is_prime(199))
        self.assertTrue(is_prime(211))
        self.assertTrue(is_prime(221))
        self.assertTrue(is_prime(223))
        self.assertTrue(is_prime(227))
        self.assertTrue(is_prime(229))
        self.assertTrue(is_prime(233))
        self.assertTrue(is_prime(239))
        self.assertTrue(is_prime(241))
        self.assertTrue(is_prime(251))
        self.assertTrue(is_prime(257))
        self.assertTrue(is_prime(263))
        self.assertTrue(is_prime(269))
        self.assertTrue(is_prime(271))
        self.assertTrue(is_prime(277))
        self.assertTrue(is_prime(281))
        self.assertTrue(is_prime(283))
        self.assertTrue(is_prime(293))
        self.assertTrue(is_prime(299))
        self.assertTrue(is_prime(307))
        self.assertTrue(is_prime(311))
        self.assertTrue(is_prime(313))
        self.assertTrue(is_prime(317))
        self.assertTrue(is_prime(331))
        self.assertTrue(is_prime(337))
        self.assertTrue(is_prime(347))
        self.assertTrue(is_prime(349))
        self.assertTrue(is_prime(353))
        self.assertTrue(is_prime(359))
        self.assertTrue(is_prime(367))
        self.assertTrue(is_prime(373))
        self.assertTrue(is_prime(379))
        self.assertTrue(is_prime(383))
        self.assertTrue(is_prime(389))
        self.assertTrue(is_prime(397))
        self.assertTrue(is_prime(401))
        self.assertTrue(is_prime(409))
        self.assertTrue(is_prime(419))
        self.assertTrue(is_prime(421))
        self.assertTrue(is_prime(431))
        self.assertTrue(is_prime(433))
        self.assertTrue(is_prime(439))
        self.assertTrue(is_prime(443))
        self.assertTrue(is_prime(449))
        self.assertTrue(is_prime(457))
        self.assertTrue(is_prime(461))
        self.assertTrue(is_prime(463))
        self.assertTrue(is_prime(467))
        self.assertTrue(is_prime(479))
        self.assertTrue(is_prime(487))
        self.assertTrue(is_prime(491))
        self.assertTrue(is_prime(499))
        self.assertTrue(is_prime(503))
        self.assertTrue(is_prime(509))
        self.assertTrue(is_prime(521))
        self.assertTrue(is_prime(523))
        self.assertTrue(is_prime(541))
        self.assertTrue(is_prime(547))
        self.assertTrue(is_prime(557))
        self.assertTrue(is_prime(563