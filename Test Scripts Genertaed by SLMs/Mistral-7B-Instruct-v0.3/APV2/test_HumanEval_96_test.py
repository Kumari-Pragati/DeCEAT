You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_96_code import count_up_to
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_up_to(n):
    """Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    For example:
    count_up_to(5) => [2, 3]
    count_up_to(11) => [2, 3, 5, 7]
    count_up_to(0) => []
    count_up_to(20) => [2, 3, 5, 7, 11, 13, 17, 19]
    count_up_to(1) => []
    count_up_to(18) => [2, 3, 5, 7, 11, 13, 17]
    """

    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

 Here is a complete unittest test suite for the `count_up_to` function:


import unittest
from HumanEval_96_code import count_up_to

class TestCountUpTo(unittest.TestCase):

    def test_count_up_to_zero(self):
        self.assertListEqual(count_up_to(0), [])

    def test_count_up_to_one(self):
        self.assertListEqual(count_up_to(1), [])

    def test_count_up_to_two(self):
        self.assertListEqual(count_up_to(2), [2])

    def test_count_up_to_three(self):
        self.assertListEqual(count_up_to(3), [2])

    def test_count_up_to_four(self):
        self.assertListEqual(count_up_to(4), [2])

    def test_count_up_to_five(self):
        self.assertListEqual(count_up_to(5), [2, 3])

    def test_count_up_to_six(self):
        self.assertListEqual(count_up_to(6), [2, 3])

    def test_count_up_to_seven(self):
        self.assertListEqual(count_up_to(7), [2, 3])

    def test_count_up_to_eight(self):
        self.assertListEqual(count_up_to(8), [2, 3])

    def test_count_up_to_nine(self):
        self.assertListEqual(count_up_to(9), [2, 3])

    def test_count_up_to_ten(self):
        self.assertListEqual(count_up_to(10), [2, 3, 5])

    def test_count_up_to_eleven(self):
        self.assertListEqual(count_up_to(11), [2, 3, 5, 7])

    def test_count_up_to_twelve(self):
        self.assertListEqual(count_up_to(12), [2, 3, 5, 7])

    def test_count_up_to_thirteen(self):
        self.assertListEqual(count_up_to(13), [2, 3, 5, 7])

    def test_count_up_to_fourteen(self):
        self.assertListEqual(count_up_to(14), [2, 3, 5, 7])

    def test_count_up_to_fifteen(self):
        self.assertListEqual(count_up_to(15), [2, 3, 5, 7])

    def test_count_up_to_twenty(self):
        self.assertListEqual(count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_count_up_to_twenty_one(self):
        self.assertListEqual(count_up_to(21), [2, 3, 5, 7, 11, 13, 17])

    def test_count_up_to_one_hundred(self):
        self.assertListEqual(count_up_to(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various edge cases and a range of inputs, ensuring that the `count_up_to` function behaves as expected.