user

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
    return sorted(odd_digit_elements)assistant

Here is the unittest test script for the `unique_digits` function:

import unittest
from HumanEval_104_code import unique_digits

class TestUniqueDigits(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(unique_digits([]), [])

    def test_single_element(self):
        self.assertEqual(unique_digits([15]), [15])

    def test_multiple_elements(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_no_odd_digits(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_mixed_results(self):
        self.assertEqual(unique_digits([15, 33, 1422, 152, 1, 10]), [1, 15, 33])

    def test_large_input(self):
        self.assertEqual(unique_digits([15, 33, 1422, 152, 1, 10, 123, 456, 789]), [1, 15, 33, 123, 789])

if __name__ == '__main__':
    unittest.main()

This test script covers various scenarios, including:

1. An empty list as input
2. A single element with an odd digit
3. Multiple elements with odd digits
4. No elements with odd digits
5. A mixed input with both odd and even digits
6. A large input with multiple elements

Each test case uses the `assertEqual` method to verify that the output of the `unique_digits` function matches the expected result.