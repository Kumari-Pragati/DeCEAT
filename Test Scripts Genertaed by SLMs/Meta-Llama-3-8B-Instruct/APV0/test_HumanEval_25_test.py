user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_25_code import factorize
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return factassistant

Here is a unittest test script for the given Python function:

Python
import unittest
from HumanEval_25_code import factorize

class TestFactorize(unittest.TestCase):

    def test_factorize(self):
        self.assertEqual(factorize(8), [2, 2, 2])
        self.assertEqual(factorize(25), [5, 5])
        self.assertEqual(factorize(70), [2, 5, 7])
        self.assertEqual(factorize(1), [1])
        self.assertEqual(factorize(2), [2])
        self.assertEqual(factorize(3), [3])
        self.assertEqual(factorize(4), [2, 2])
        self.assertEqual(factorize(5), [5])
        self.assertEqual(factorize(6), [2, 3])
        self.assertEqual(factorize(7), [7])
        self.assertEqual(factorize(8), [2, 2, 2])
        self.assertEqual(factorize(9), [3, 3])
        self.assertEqual(factorize(10), [2, 5])
        self.assertEqual(factorize(11), [11])
        self.assertEqual(factorize(12), [2, 2, 3])
        self.assertEqual(factorize(13), [13])
        self.assertEqual(factorize(14), [2, 7])
        self.assertEqual(factorize(15), [3, 5])
        self.assertEqual(factorize(16), [2, 2, 2, 2])
        self.assertEqual(factorize(17), [17])
        self.assertEqual(factorize(18), [2, 3, 3])
        self.assertEqual(factorize(19), [19])
        self.assertEqual(factorize(20), [2, 2, 5])
        self.assertEqual(factorize(21), [3, 7])
        self.assertEqual(factorize(22), [2, 11])
        self.assertEqual(factorize(23), [23])
        self.assertEqual(factorize(24), [2, 2, 2, 3])
        self.assertEqual(factorize(25), [5, 5])
        self.assertEqual(factorize(26), [2, 13])
        self.assertEqual(factorize(27), [3, 3, 3])
        self.assertEqual(factorize(28), [2, 2, 7])
        self.assertEqual(factorize(29), [29])
        self.assertEqual(factorize(30), [2, 3, 5])
        self.assertEqual(factorize(31), [31])
        self.assertEqual(factorize(32), [2, 2, 2, 2, 2])
        self.assertEqual(factorize(33), [3, 11])
        self.assertEqual(factorize(34), [2, 17])
        self.assertEqual(factorize(35), [5, 7])
        self.assertEqual(factorize(36), [2, 2, 3, 3])
        self.assertEqual(factorize(37), [37])
        self.assertEqual(factorize(38), [2, 19])
        self.assertEqual(factorize(39), [3, 13])
        self.assertEqual(factorize(40), [2, 2, 2, 5])
        self.assertEqual(factorize(41), [41])
        self.assertEqual(factorize(42), [2, 3, 7])
        self.assertEqual(factorize(43), [43])
        self.assertEqual(factorize(44), [2, 2, 11])
        self.assertEqual(factorize(45), [3, 3, 5])
        self.assertEqual(factorize(46), [2, 23])
        self.assertEqual(factorize(47), [47])
        self.assertEqual(factorize(48), [2, 2, 2, 2, 3])
        self.assertEqual(factorize(49), [7, 7])
        self.assertEqual(factorize(50), [2, 5, 5])
        self.assertEqual(factorize(51), [3, 17])
        self.assertEqual(factorize(52), [2, 2, 13])
        self.assertEqual(factorize(53), [53])
        self.assertEqual(factorize(54), [2, 3, 3, 3])
        self.assertEqual(factorize(55), [5, 11])
        self.assertEqual(factorize(56), [2, 2, 2, 7])
        self.assertEqual(factorize(57), [3, 19])
        self.assertEqual(factorize(58), [2, 29])
        self.assertEqual(factorize(59), [59])
        self.assertEqual(factorize(60), [2, 2, 3, 5])
        self.assertEqual(factorize(61), [61])
        self.assertEqual(factorize(62), [2, 31])
        self.assertEqual(factorize(63), [3, 3, 7])
        self.assertEqual(factorize(64), [2