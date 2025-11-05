You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
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

 Here is the complete unittest test suite for the `add_elements` function:


import unittest
from HumanEval_122_code import add_elements

class TestAddElements(unittest.TestCase):

    def test_add_elements_basic(self):
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)
        self.assertEqual(add_elements([1, 2, 3, 4000, 5, 6, 7, 8, 9], 8), 15)
        self.assertEqual(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 15)
        self.assertEqual(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 1), 3)

    def test_add_elements_empty_list(self):
        self.assertEqual(add_elements([], 1), 0)

    def test_add_elements_single_element(self):
        self.assertEqual(add_elements([1], 1), 1)
        self.assertEqual(add_elements([11], 1), 11)
        self.assertEqual(add_elements([111], 1), 111)

    def test_add_elements_k_greater_than_len(self):
        self.assertEqual(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 10), 15)

    def test_add_elements_k_equal_to_len(self):
        self.assertEqual(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 15)

    def test_add_elements_large_numbers(self):
        self.assertEqual(add_elements([1, 2, 3, 4000000, 5, 6, 7, 8, 9], 8), 18)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as basic usage, empty lists, single elements, k greater than len(arr), k equal to len(arr), and large numbers.