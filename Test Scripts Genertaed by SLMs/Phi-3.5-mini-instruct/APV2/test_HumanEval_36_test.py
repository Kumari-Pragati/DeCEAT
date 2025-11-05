You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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

 import unittest
from HumanEval_36_code import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz_zero(self):
        self.assertEqual(fizz_buzz(50), 0)

    def test_fizz_buzz_divisible_by_11_or_13(self):
        self.assertEqual(fizz_buzz(78), 2)

    def test_fizz_buzz_divisible_by_11_and_13(self):
        self.assertEqual(fizz_buzz(79), 3)

    def test_fizz_buzz_divisible_by_11(self):
        self.assertEqual(fizz_buzz(77), 1)

    def test_fizz_buzz_divisible_by_13(self):
        self.assertEqual(fizz_buzz(82), 1)

    def test_fizz_buzz_divisible_by_11_and_13_twice(self):
        self.assertEqual(fizz_buzz(143), 2)

    def test_fizz_buzz_divisible_by_11_and_13_three_times(self):
        self.assertEqual(fizz_buzz(156), 3)

    def test_fizz_buzz_divisible_by_11_and_13_four_times(self):
        self.assertEqual(fizz_buzz(169), 4)

    def test_fizz_buzz_divisible_by_11_and_13_five_times(self):
        self.assertEqual(fizz_buzz(182), 5)

    def test_fizz_buzz_divisible_by_11_and_13_six_times(self):
        self.assertEqual(fizz_buzz(195), 6)

    def test_fizz_buzz_divisible_by_11_and_13_seven_times(self):
        self.assertEqual(fizz_buzz(208), 7)

    def test_fizz_buzz_divisible_by_11_and_13_eight_times(self):
        self.assertEqual(fizz_buzz(221), 8)

    def test_fizz_buzz_divisible_by_11_and_13_nine_times(self):
        self.assertEqual(fizz_buzz(234), 9)

    def test_fizz_buzz_divisible_by_11_and_13_ten_times(self):
        self.assertEqual(fizz_buzz(247), 10)

if __name__ == '__main__':
    unittest.main()