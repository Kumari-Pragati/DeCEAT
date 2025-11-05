You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_146_code import specialFilter
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
    return count


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_146_code import specialFilter

class TestSpecialFilter(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

    def test_negative_numbers(self):
        self.assertEqual(specialFilter([-15, -73, -14, 15]), 1)
        self.assertEqual(specialFilter([-33, 2, 3, -45, -21, -109]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]), 3)
        self.assertEqual(specialFilter([-15, -73, -14, 15, -33, 2, 3, -45, -21, -109]), 1)

    def test_zero_and_single_digit_numbers(self):
        self.assertEqual(specialFilter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 0)
        self.assertEqual(specialFilter([10, 20, 30, 40, 50, 60, 70, 80, 90]), 0)

    def test_large_numbers(self):
        self.assertEqual(specialFilter([1000000001, 1000000003, 1000000005, 1000000007, 1000000009]), 5)
        self.assertEqual(specialFilter([-1000000001, -1000000003, -1000000005, -1000000007, -1000000009]), 0)

if __name__ == '__main__':
    unittest.main()


This suite includes tests for positive numbers, negative numbers, mixed numbers, single-digit numbers, and large numbers. It checks if the function correctly identifies the numbers that are greater than 10 and have both the first and last digits as odd numbers.