system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_122_code import add_elements

class TestAddElements(unittest.TestCase):

    def test_add_elements(self):
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)
        self.assertEqual(add_elements([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(add_elements([100, 200, 300, 400, 500], 5), 1500)
        self.assertEqual(add_elements([10, 20, 30, 40, 50, 60, 70, 80, 90], 9, 100), 210)
        self.assertEqual(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 45)
        self.assertEqual(add_elements([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], 10), 2550)
        self.assertEqual(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 90)
        self.assertEqual(add_elements([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500], 15), 4500)
        self.assertEqual(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20), 210)
        self.assertEqual(add_elements([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000], 20), 10500)

    def test_add_elements_invalid_input(self):
        with self.assertRaises(TypeError):
            add_elements([], 4)
        with self.assertRaises(TypeError):
            add_elements([1, 2, 3, 4, 5], None)
        with self.assertRaises(TypeError):
            add_elements([1, 2, 3, 4, 5], 'four')

if __name__ == '__main__':
    unittest.main()