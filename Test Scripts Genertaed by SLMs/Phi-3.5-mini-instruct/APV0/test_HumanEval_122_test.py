Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_122_code import add_elements
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)

 import unittest
from HumanEval_122_code import add_elements

class TestAddElements(unittest.TestCase):

    def test_sum_of_elements_with_two_digits(self):
        arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
        k = 4
        expected_output = 24  # sum of 21 + 3
        self.assertEqual(add_elements(arr, k), expected_output)

    def test_sum_of_elements_with_two_digits_at_end(self):
        arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
        k = 9
        expected_output = 21  # sum of all elements since k is the length of the array
        self.assertEqual(add_elements(arr, k), expected_output)

    def test_sum_of_elements_with_two_digits_empty_array(self):
        arr = []
        k = 5
        expected_output = 0
        self.assertEqual(add_elements(arr, k), expected_output)

    def test_sum_of_elements_with_two_digits_single_element(self):
        arr = [111]
        k = 1
        expected_output = 111
        self.assertEqual(add_elements(arr, k), expected_output)

    def test_sum_of_elements_with_two_digits_no_elements(self):
        arr = []
        k = 0
        expected_output = 0
        self.assertEqual(add_elements(arr, k), expected_output)

    def test_sum_of_elements_with_two_digits_all_elements(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        k = 9
        expected_output = 45
        self.assertEqual(add_elements(arr, k), expected_output)

    def test_sum_of_elements_with_two_digits_negative_numbers(self):
        arr = [-111, -21, 3, -4000, 5, 6, 7, 8, 9]
        k = 4
        expected_output = -92  # sum of -111 + -21 + 3
        self.assertEqual(add_elements(arr, k), expected_output)

if __name__ == '__main__':
    unittest.main()