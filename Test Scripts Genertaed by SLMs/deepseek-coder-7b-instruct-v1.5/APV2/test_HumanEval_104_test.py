You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_104_code import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_all_odd_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_all_even_digits(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_mixed_digits(self):
        self.assertEqual(unique_digits([152, 33, 1422, 10]), [33])

    def test_single_digit_elements(self):
        self.assertEqual(unique_digits([1, 3, 5, 7, 9]), sorted([1, 3, 5, 7, 9]))

    def test_empty_list(self):
        self.assertEqual(unique_digits([]), [])

    def test_negative_numbers(self):
        self.assertEqual(unique_digits([-15, -33, -1422, -1]), [])

    def test_zero(self):
        self.assertEqual(unique_digits([0]), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various scenarios including:

- All odd digits
- All even digits
- Mixed odd and even digits
- Single digit elements
- Empty list
- Negative numbers
- Zero

Each test verifies that the function's output matches the expected result.