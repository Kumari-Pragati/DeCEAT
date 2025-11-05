You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)

    def test_sum_of_elements_with_two_digits_empty_array(self):
        self.assertEqual(add_elements([], 4), 0)

    def test_sum_of_elements_with_two_digits_k_greater_than_array_length(self):
        self.assertEqual(add_elements([1, 2, 3], 10), 3)

    def test_sum_of_elements_with_two_digits_k_equals_array_length(self):
        self.assertEqual(add_elements([1, 2, 3], 3), 6)

    def test_sum_of_elements_with_two_digits_k_less_than_one(self):
        self.assertEqual(add_elements([1, 2, 3], 0), 0)

    def test_sum_of_elements_with_two_digits_all_elements_have_more_than_two_digits(self):
        self.assertEqual(add_elements([100, 2000, 30000], 3), 0)

    def test_sum_of_elements_with_two_digits_k_equals_one(self):
        self.assertEqual(add_elements([100], 1), 0)

if __name__ == '__main__':
    unittest.main()