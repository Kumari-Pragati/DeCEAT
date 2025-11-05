user

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
    return sorted(odd_collatz)assistant

Here is the unittest test script for the `get_odd_collatz` function:

import unittest
from HumanEval_123_code import get_odd_collatz

class TestGetOddCollatz(unittest.TestCase):
    def test_get_odd_collatz(self):
        # Test case 1: n = 5
        self.assertEqual(get_odd_collatz(5), [1, 5])

        # Test case 2: n = 2
        self.assertEqual(get_odd_collatz(2), [])

        # Test case 3: n = 1
        self.assertEqual(get_odd_collatz(1), [1])

        # Test case 4: n = 10
        self.assertEqual(get_odd_collatz(10), [1, 3, 5, 17, 53, 161, 485, 1461, 485, 1461, 1])

        # Test case 5: n = 20
        self.assertEqual(get_odd_collatz(20), [1, 3, 5, 7, 13, 21, 65, 197, 593, 1781, 541, 1625, 1])

        # Test case 6: n = 30
        self.assertEqual(get_odd_collatz(30), [1, 3, 5, 7, 11, 17, 23, 35, 53, 79, 239, 718, 359, 1])

if __name__ == '__main__':
    unittest.main()

This script defines a `TestGetOddCollatz` class that contains six test cases for the `get_odd_collatz` function. Each test case checks the output of the function for a specific input value of `n`. The `assertEqual` method is used to compare the expected output with the actual output of the function.

You can run this script directly to execute the tests and verify that the `get_odd_collatz` function is working correctly.