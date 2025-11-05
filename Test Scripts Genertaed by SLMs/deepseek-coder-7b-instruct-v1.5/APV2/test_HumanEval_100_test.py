You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_100_code import make_a_pile
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """

    return [n + 2*i for i in range(n)]


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_100_code import make_a_pile

class TestMakeAPile(unittest.TestCase):

    def test_make_a_pile_with_odd_number(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])

    def test_make_a_pile_with_even_number(self):
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])

    def test_make_a_pile_with_zero(self):
        self.assertEqual(make_a_pile(0), [])

    def test_make_a_pile_with_negative_number(self):
        with self.assertRaises(Exception):
            make_a_pile(-1)

    def test_make_a_pile_with_large_number(self):
        self.assertEqual(make_a_pile(1000), list(range(3, 2003, 2)))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- A positive odd number
- A positive even number
- Zero
- A negative number
- A large number

The test_make_a_pile_with_negative_number test checks if the function raises an exception when a negative number is given. The test_make_a_pile_with_large_number test checks if the function returns the correct list for a large number.

Please note that the function make_a_pile(0) should return an empty list, but the function make_a_pile(n) generates a list with n elements. So, the test_make_a_pile_with_zero test checks if the function returns an empty list when 0 is given.

Also, the function make_a_pile(n) generates a list with n elements. So, the test_make_a_pile_with_large_number test checks if the function returns the correct list for a large number.

The test_make_a_pile_with_negative_number test checks if the function raises an exception when a negative number is given. The function make_a_pile(n) does not handle negative numbers, so it should raise an exception when a negative number is given.

The test_make_a_pile_with_odd_number and test_make_a_pile_with_even_number tests check if the function returns the correct list for odd and even numbers, respectively.

The unittest module is a built-in Python library for testing, and it provides a rich set of tools for constructing and running tests.