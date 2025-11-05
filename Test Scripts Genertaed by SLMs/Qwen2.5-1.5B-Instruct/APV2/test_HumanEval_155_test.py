system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Provided function
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_even_odd_count(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(123), (1, 2))
        self.assertEqual(even_odd_count(0), (1, 0))
        self.assertEqual(even_odd_count(2468), (4, 0))

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure the `even_odd_count` function works correctly across various inputs, including negative numbers, zero, and positive numbers with different digit counts.