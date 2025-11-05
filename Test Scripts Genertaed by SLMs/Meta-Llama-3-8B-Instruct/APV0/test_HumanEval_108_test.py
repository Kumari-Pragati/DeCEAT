user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_108_code import count_nums

class TestCountNums(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(count_nums([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_nums([-1, 11, -11]), 1)

    def test_positive_numbers(self):
        self.assertEqual(count_nums([1, 1, 2]), 3)

    def test_mixed_numbers(self):
        self.assertEqual(count_nums([-1, 11, 2, -11, 3]), 3)

    def test_single_negative_number(self):
        self.assertEqual(count_nums([-1]), 0)

    def test_single_positive_number(self):
        self.assertEqual(count_nums([1]), 1)

    def test_single_zero(self):
        self.assertEqual(count_nums([0]), 0)

    def test_multiple_zero(self):
        self.assertEqual(count_nums([0, 0, 0]), 0)

    def test_multiple_negative_numbers(self):
        self.assertEqual(count_nums([-1, -2, -3]), 0)

    def test_multiple_positive_numbers(self):
        self.assertEqual(count_nums([1, 2, 3]), 3)

    def test_multiple_mixed_numbers(self):
        self.assertEqual(count_nums([-1, 2, 3, -4, 5]), 4)

if __name__ == '__main__':
    unittest.main()


This script includes 11 test cases to cover different scenarios, including empty array, negative numbers, positive numbers, mixed numbers, single negative number, single positive number, single zero, multiple zero, multiple negative numbers, multiple positive numbers, and multiple mixed numbers.