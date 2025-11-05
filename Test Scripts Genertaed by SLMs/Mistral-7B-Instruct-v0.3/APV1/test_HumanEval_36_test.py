You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_36_code import fizz_buzz

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans

 Here is a comprehensive unittest test suite for the given Python function `fizz_buzz`. I've included a variety of test cases to cover different scenarios and edge cases.


import unittest
from HumanEval_36_code import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz_zero(self):
        self.assertEqual(fizz_buzz(0), 0)

    def test_fizz_buzz_negative(self):
        self.assertEqual(fizz_buzz(-1), 0)

    def test_fizz_buzz_small_positive(self):
        self.assertEqual(fizz_buzz(1), 0)
        self.assertEqual(fizz_buzz(2), 0)
        self.assertEqual(fizz_buzz(3), 0)
        self.assertEqual(fizz_buzz(4), 0)
        self.assertEqual(fizz_buzz(5), 0)
        self.assertEqual(fizz_buzz(6), 0)
        self.assertEqual(fizz_buzz(7), 0)
        self.assertEqual(fizz_buzz(8), 0)
        self.assertEqual(fizz_buzz(9), 0)
        self.assertEqual(fizz_buzz(10), 0)
        self.assertEqual(fizz_buzz(11), 0)
        self.assertEqual(fizz_buzz(12), 0)

    def test_fizz_buzz_small_positive_with_7(self):
        self.assertEqual(fizz_buzz(7), 1)
        self.assertEqual(fizz_buzz(17), 1)

    def test_fizz_buzz_small_positive_with_11(self):
        self.assertEqual(fizz_buzz(11), 0)
        self.assertEqual(fizz_buzz(22), 1)
        self.assertEqual(fizz_buzz(33), 2)
        self.assertEqual(fizz_buzz(44), 3)
        self.assertEqual(fizz_buzz(55), 4)
        self.assertEqual(fizz_buzz(66), 5)
        self.assertEqual(fizz_buzz(77), 6)

    def test_fizz_buzz_small_positive_with_13(self):
        self.assertEqual(fizz_buzz(13), 0)
        self.assertEqual(fizz_buzz(26), 1)
        self.assertEqual(fizz_buzz(39), 2)
        self.assertEqual(fizz_buzz(52), 3)
        self.assertEqual(fizz_buzz(65), 4)
        self.assertEqual(fizz_buzz(78), 5)

    def test_fizz_buzz_small_positive_with_11_and_13(self):
        self.assertEqual(fizz_buzz(22), 1)
        self.assertEqual(fizz_buzz(33), 2)
        self.assertEqual(fizz_buzz(44), 3)
        self.assertEqual(fizz_buzz(55), 4)
        self.assertEqual(fizz_buzz(66), 5)

    def test_fizz_buzz_large_positive(self):
        self.assertEqual(fizz_buzz(100), 7)
        self.assertEqual(fizz_buzz(200), 17)
        self.assertEqual(fizz_buzz(300), 27)
        self.assertEqual(fizz_buzz(400), 37)
        self.assertEqual(fizz_buzz(500), 47)
        self.assertEqual(fizz_buzz(600), 57)
        self.assertEqual(fizz_buzz(700), 67)
        self.assertEqual(fizz_buzz(800), 77)
        self.assertEqual(fizz_buzz(900), 87)