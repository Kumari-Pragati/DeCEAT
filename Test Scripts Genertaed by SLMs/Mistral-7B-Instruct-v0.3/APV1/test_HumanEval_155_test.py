You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_even_odd_count(self):
        self.assertEqual(even_odd_count(0), (1, 0))
        self.assertEqual(even_odd_count(1), (0, 1))
        self.assertEqual(even_odd_count(2), (1, 1))
        self.assertEqual(even_odd_count(3), (0, 1))
        self.assertEqual(even_odd_count(4), (1, 1))
        self.assertEqual(even_odd_count(5), (0, 1))
        self.assertEqual(even_odd_count(10), (2, 2))
        self.assertEqual(even_odd_count(11), (0, 2))
        self.assertEqual(even_odd_count(12), (1, 2))
        self.assertEqual(even_odd_count(13), (0, 2))
        self.assertEqual(even_odd_count(-1), (0, 1))
        self.assertEqual(even_odd_count(-2), (1, 1))
        self.assertEqual(even_odd_count(-3), (0, 1))
        self.assertEqual(even_odd_count(-4), (1, 1))
        self.assertEqual(even_odd_count(-5), (0, 1))
        self.assertEqual(even_odd_count(-10), (2, 2))
        self.assertEqual(even_odd_count(-11), (0, 2))
        self.assertEqual(even_odd_count(-12), (1, 2))
        self.assertEqual(even_odd_count(-13), (0, 2))
        self.assertEqual(even_odd_count(-123), (1, 3))
        self.assertEqual(even_odd_count(-120), (2, 2))
        self.assertEqual(even_odd_count(-1200), (4, 4))

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases for positive and negative integers with different numbers of even and odd digits. It uses the `assertEqual` method to check if the output of the `even_odd_count` function matches the expected output for each test case.