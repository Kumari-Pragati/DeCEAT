You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_108_code import count_nums

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    def digits_sum(n):
        neg = 1
        if n < 0:
            n, neg = -1 * n, -1
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)

    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_108_code import count_nums

class TestCountNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_nums([]), 0)

    def test_single_positive_number(self):
        self.assertEqual(count_nums([1]), 1)

    def test_single_negative_number(self):
        self.assertEqual(count_nums([-1]), 1)

    def test_multiple_numbers(self):
        self.assertEqual(count_nums([1, -1, 12, -12, 123, -123]), 3)

    def test_large_numbers(self):
        self.assertEqual(count_nums([123456789, -987654321]), 2)

    def test_mixed_numbers(self):
        self.assertEqual(count_nums([1, -1, 12, -12, 123, -123, 987654321, -987654321]), 4)

if __name__ == '__main__':
    unittest.main()


This suite includes tests for different scenarios:

- An empty list
- A list with a single positive number
- A list with a single negative number
- A list with multiple numbers, including both positive and negative
- A list with large numbers
- A list with a mix of positive and negative numbers

Each test case checks that the output of the `count_nums` function matches the expected result.