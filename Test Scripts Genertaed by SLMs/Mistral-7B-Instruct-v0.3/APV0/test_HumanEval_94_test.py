Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_94_code import skjkasdkd
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """

    def isPrime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    maxx = 0
    i = 0
    while i < len(lst):
        if lst[i] > maxx and isPrime(lst[i]):
            maxx = lst[i]
        i += 1

    result = sum(int(digit) for digit in str(maxx))
    return result

 Here is a unittest test script for the provided function `skjkasdkd`. The test script includes several test cases to cover various scenarios and edge cases.


import unittest
from HumanEval_94_code import skjkasdkd

class TestSkjkasdkd(unittest.TestCase):

    def test_skjkasdkd_example1(self):
        self.assertEqual(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]), 10)

    def test_skjkasdkd_example2(self):
        self.assertEqual(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]), 25)

    def test_skjkasdkd_example3(self):
        self.assertEqual(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]), 13)

    def test_skjkasdkd_example4(self):
        self.assertEqual(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6]), 11)

    def test_skjkasdkd_example5(self):
        self.assertEqual(skjkasdkd([0,81,12,3,1,21]), 3)

    def test_skjkasdkd_example6(self):
        self.assertEqual(skjkasdkd([0,8,1,2,1,7]), 7)

    def test_skjkasdkd_empty_list(self):
        self.assertEqual(skjkasdkd([]), 0)

    def test_skjkasdkd_single_element_list(self):
        self.assertEqual(skjkasdkd([1]), 1)

    def test_skjkasdkd_all_zeroes(self):
        self.assertEqual(skjkasdkd([0]), 0)

    def test_skjkasdkd_all_non_primes(self):
        self.assertEqual(skjkasdkd([2, 4, 6]), 6)

    def test_skjkasdkd_all_primes(self):
        self.assertEqual(skjkasdkd([2, 3, 5, 7]), 17)

if __name__ == '__main__':
    unittest.main()


This test script includes test cases for the provided examples, as well as additional test cases to cover edge cases such as an empty list, a single-element list, a list of all zeroes, a list of all non-primes, and a list of all primes.