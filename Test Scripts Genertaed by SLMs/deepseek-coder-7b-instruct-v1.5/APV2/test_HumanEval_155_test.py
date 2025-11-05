You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_155_code import even_odd_count
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(even_odd_count(123), (1, 2))

    def test_negative_number(self):
        self.assertEqual(even_odd_count(-12), (1, 1))

    def test_zero(self):
        self.assertEqual(even_odd_count(0), (1, 0))

    def test_single_digit_even(self):
        self.assertEqual(even_odd_count(4), (1, 0))

    def test_single_digit_odd(self):
        self.assertEqual(even_odd_count(5), (0, 1))

    def test_all_even_digits(self):
        self.assertEqual(even_odd_count(2468), (4, 0))

    def test_all_odd_digits(self):
        self.assertEqual(even_odd_count(13579), (0, 5))

    def test_mixed_digits(self):
        self.assertEqual(even_odd_count(123456), (3, 3))

if __name__ == '__main__':
    unittest.main()


This suite includes tests for various scenarios including positive and negative numbers, zero, single-digit even and odd numbers, numbers with all even or odd digits, and numbers with mixed even and odd digits.