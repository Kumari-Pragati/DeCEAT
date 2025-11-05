You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the `specialFilter` function:


import unittest
from HumanEval_146_code import specialFilter

class TestSpecialFilter(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(specialFilter([]), 0)

    def test_single_number(self):
        self.assertEqual(specialFilter([1]), 0)
        self.assertEqual(specialFilter([11]), 0)
        self.assertEqual(specialFilter([10]), 0)
        self.assertEqual(specialFilter([15]), 0)

    def test_numbers_less_than_10(self):
        self.assertEqual(specialFilter([-73, -2, -3]), 0)

    def test_numbers_greater_than_10_with_even_digits(self):
        self.assertEqual(specialFilter([14, -15]), 0)
        self.assertEqual(specialFilter([21]), 0)
        self.assertEqual(specialFilter([109]), 0)

    def test_numbers_greater_than_10_with_odd_digits(self):
        self.assertEqual(specialFilter([15]), 1)
        self.assertEqual(specialFilter([33]), 0)
        self.assertEqual(specialFilter([45]), 1)
        self.assertEqual(specialFilter([109]), 0)

    def test_numbers_with_leading_zero(self):
        self.assertEqual(specialFilter([015]), 0)
        self.assertEqual(specialFilter([033]), 1)
        self.assertEqual(specialFilter([045]), 1)
        self.assertEqual(specialFilter([0109]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]), 2)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty list, single numbers, numbers less than 10, numbers greater than 10 with even digits, numbers greater than 10 with odd digits, numbers with leading zeros, and a mix of numbers.