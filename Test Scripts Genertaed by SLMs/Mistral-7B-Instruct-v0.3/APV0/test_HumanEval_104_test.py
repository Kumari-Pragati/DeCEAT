Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `unique_digits` function:


import unittest
from HumanEval_104_code import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(unique_digits([]), [])

    def test_single_element(self):
        self.assertListEqual(unique_digits([1]), [1])

    def test_single_odd_element(self):
        self.assertListEqual(unique_digits([15]), [15])

    def test_multiple_odd_elements(self):
        self.assertListEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_multiple_even_elements(self):
        self.assertListEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_multiple_elements_with_odd_and_even(self):
        self.assertListEqual(unique_digits([152, 323, 1422, 1, 5]), [1, 5])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover various scenarios, including an empty list, a single element, multiple odd elements, multiple even elements, and a mix of odd and even elements. The test cases use the `assertListEqual` method to verify that the expected output matches the actual output produced by the `unique_digits` function.