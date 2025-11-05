You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(even_odd_count(123), (1, 2))
        self.assertEqual(even_odd_count(456), (2, 1))
        self.assertEqual(even_odd_count(789), (1, 2))

    def test_negative_numbers(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(-456), (2, 1))
        self.assertEqual(even_odd_count(-789), (1, 2))

    def test_single_digit_numbers(self):
        self.assertEqual(even_odd_count(0), (1, 0))
        self.assertEqual(even_odd_count(5), (0, 1))
        self.assertEqual(even_odd_count(6), (1, 0))

    def test_large_numbers(self):
        self.assertEqual(even_odd_count(1234567890), (5, 4))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive numbers, negative numbers, single-digit numbers, and large numbers. It checks that the function returns the correct number of even and odd digits for each of these cases.