You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_104_code import unique_digits
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    odd_digit_elements = []
    for i in x:
        if all(int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)

 Here is the complete unittest test suite for the `unique_digits` function:


import unittest
from HumanEval_104_code import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(unique_digits([]), [])

    def test_single_element(self):
        self.assertListEqual(unique_digits([1]), [1])

    def test_single_even_element(self):
        self.assertListEqual(unique_digits([2]), [])

    def test_multiple_elements_with_odd_digits(self):
        self.assertListEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_multiple_elements_with_even_digits(self):
        self.assertListEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_multiple_elements_with_mixed_odd_and_even_digits(self):
        self.assertListEqual(unique_digits([152, 323, 1422, 1, 5]), [1, 5])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty list, a single element, single even element, multiple elements with odd digits, multiple elements with even digits, and multiple elements with mixed odd and even digits.