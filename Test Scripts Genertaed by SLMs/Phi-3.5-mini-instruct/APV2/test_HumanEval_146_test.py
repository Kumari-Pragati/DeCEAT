You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 
import unittest
from HumanEval_146_code import specialFilter

class TestSpecialFilter(unittest.TestCase):

    def test_specialFilter_with_positive_numbers(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)

    def test_specialFilter_with_negative_numbers(self):
        self.assertEqual(specialFilter([-33, -2, -3, 45, 21, 109]), 2)

    def test_specialFilter_with_numbers_less_than_10(self):
        self.assertEqual(specialFilter([9, 8, 7, 6, 5]), 0)

    def test_specialFilter_with_no_qualifying_numbers(self):
        self.assertEqual(specialFilter([11, 13, 15, 17]), 4)

    def test_specialFilter_with_single_qualifying_number(self):
        self.assertEqual(specialFilter([11, 21, 31, 41]), 4)

    def test_specialFilter_with_empty_list(self):
        self.assertEqual(specialFilter([]), 0)

    def test_specialFilter_with_single_element_list(self):
        self.assertEqual(specialFilter([11]), 1)

    def test_specialFilter_with_all_qualifying_numbers(self):
        self.assertEqual(specialFilter([11, 13, 15, 17, 31, 51]), 6)

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of cases to ensure that the `specialFilter` function behaves as expected. It tests with positive and negative numbers, numbers less than 10, an empty list, a single-element list, and a list where all elements are qualifying numbers. Each test case uses `self.assertEqual` to compare the expected output with the actual output from the `specialFilter` function.