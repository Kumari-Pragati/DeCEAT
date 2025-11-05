You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 import unittest
from HumanEval_104_code import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_unique_digits_with_odd_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_unique_digits_with_no_odd_digits(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_unique_digits_with_empty_list(self):
        self.assertEqual(unique_digits([]), [])

    def test_unique_digits_with_single_element(self):
        self.assertEqual(unique_digits([7]), [7])

    def test_unique_digits_with_negative_numbers(self):
        self.assertEqual(unique_digits([-15, -33, -1422, -1]), [-1])

    def test_unique_digits_with_mixed_integers(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1, 2, 4, 6, 8]), [1, 15, 33])

    def test_unique_digits_with_large_numbers(self):
        self.assertEqual(unique_digits([9999999999, 8888888888, 7777777777]), [9999999999])

if __name__ == '__main__':
    unittest.main()