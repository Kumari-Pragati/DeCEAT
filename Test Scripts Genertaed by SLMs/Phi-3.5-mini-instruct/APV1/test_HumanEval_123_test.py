You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_123_code import get_odd_collatz
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    if n % 2 == 0:
        odd_collatz = []
    else:
        odd_collatz = [n]
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        if n % 2 == 1:
            odd_collatz.append(int(n))
    return sorted(odd_collatz)

 import unittest
from HumanEval_123_code import get_odd_collatz

class TestGetOddCollatz(unittest.TestCase):

    def test_collatz_sequence_for_1(self):
        self.assertEqual(get_odd_collatz(1), [1])

    def test_collatz_sequence_for_5(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

    def test_collatz_sequence_for_7(self):
        self.assertEqual(get_odd_collatz(7), [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    def test_collatz_sequence_for_10(self):
        self.assertEqual(get_odd_collatz(10), [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    def test_collatz_sequence_for_15(self):
        self.assertEqual(get_odd_collatz(15), [17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    def test_collatz_sequence_for_21(self):
        self.assertEqual(get_odd_collatz(21), [21, 64, 32, 16, 8, 4, 2, 1])

    def test_collatz_sequence_for_100(self):
        self.assertEqual(get_odd_collatz(100), [155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1331, 4004, 2002, 1001, 3004, 1502, 751, 2254, 1127, 3382, 1691, 5074, 2537, 7622, 3811, 1404, 7022, 3511, 10644, 5322, 2661, 8974, 4487, 2244, 11221, 5610, 2805, 8416, 4208, 2104, 1052, 5263, 2631, 8902, 4451, 2226, 1113, 3640, 1820, 910, 455, 1366, 683, 2050, 1025, 3106, 1553, 4660, 2330, 7001, 3500, 1751, 876, 438, 219, 1095, 3286, 1643, 5410, 2705, 9116, 4558, 2279, 6838, 3419, 10265, 5132, 2566, 1283, 6420, 3210, 1605, 802, 4011, 2005, 1002, 5011, 2505, 7526