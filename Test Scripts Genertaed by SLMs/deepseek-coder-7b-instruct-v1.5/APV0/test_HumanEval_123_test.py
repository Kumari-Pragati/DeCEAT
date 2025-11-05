You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_123_code import get_odd_collatz

class TestGetOddCollatz(unittest.TestCase):
    def test_get_odd_collatz(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])
        self.assertEqual(get_odd_collatz(10), [5, 10])
        self.assertEqual(get_odd_collatz(15), [1, 5, 15])
        self.assertEqual(get_odd_collatz(20), [1, 5, 15, 20])
        self.assertEqual(get_odd_collatz(25), [1, 5, 15, 25])
        self.assertEqual(get_odd_collatz(30), [1, 5, 15, 25, 30])
        self.assertEqual(get_odd_collatz(1), [1])
        self.assertEqual(get_odd_collatz(2), [])
        self.assertEqual(get_odd_collatz(3), [3])
        self.assertEqual(get_odd_collatz(4), [1, 3])
        self.assertEqual(get_odd_collatz(6), [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 679, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827,