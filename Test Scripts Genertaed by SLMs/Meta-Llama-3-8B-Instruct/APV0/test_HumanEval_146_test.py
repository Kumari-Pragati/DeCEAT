user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return countassistant

Here is the unittest test script for the `specialFilter` function:

import unittest
from HumanEval_146_code import specialFilter

class TestSpecialFilter(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(specialFilter([]), 0)

    def test_no_numbers_greater_than_10(self):
        self.assertEqual(specialFilter([1, 2, 3, 4, 5]), 0)

    def test_no_numbers_with_odd_digits(self):
        self.assertEqual(specialFilter([11, 12, 13, 14, 15]), 0)

    def test_no_numbers_with_odd_digits_and_greater_than_10(self):
        self.assertEqual(specialFilter([11, 12, 13, 14, 15, 16]), 0)

    def test_numbers_with_odd_digits_and_greater_than_10(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)
        self.assertEqual(specialFilter([15, 33, 45, 109]), 4)

    def test_edge_cases(self):
        self.assertEqual(specialFilter([10]), 0)
        self.assertEqual(specialFilter([10.5]), 0)
        self.assertEqual(specialFilter([-10]), 0)
        self.assertEqual(specialFilter([-10.5]), 0)

if __name__ == '__main__':
    unittest.main()

This test script covers a variety of scenarios, including:

* An empty array
* An array with no numbers greater than 10
* An array with no numbers having odd digits
* An array with no numbers having odd digits and greater than 10
* An array with numbers having odd digits and greater than 10
* Edge cases such as 10, 10.5, -10, and -10.5

Each test case uses the `assertEqual` method to verify that the output of the `specialFilter` function matches the expected result.