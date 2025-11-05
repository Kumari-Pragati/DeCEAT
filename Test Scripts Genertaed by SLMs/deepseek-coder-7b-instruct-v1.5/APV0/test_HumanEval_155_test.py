You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is a unittest script for the given function:


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
        self.assertEqual(even_odd_count(3), (0, 1))

    def test_all_even_digits(self):
        self.assertEqual(even_odd_count(2222), (4, 0))

    def test_all_odd_digits(self):
        self.assertEqual(even_odd_count(1111), (0, 4))

    def test_mixed_digits(self):
        self.assertEqual(even_odd_count(1234), (2, 2))

if __name__ == '__main__':
    unittest.main()


This script creates a subclass of `unittest.TestCase` and defines several test methods that test different scenarios. Each method calls `self.assertEqual` to check that the output of `even_odd_count` matches the expected result.

Please note that you need to have the `HumanEval_155_code` module with the `even_odd_count` function defined in it for this script to work.