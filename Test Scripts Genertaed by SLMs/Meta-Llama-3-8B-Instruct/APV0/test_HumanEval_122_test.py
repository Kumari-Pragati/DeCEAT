user

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
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)assistant

Here is a unittest test script for the given Python function:

Python
import unittest
from HumanEval_122_code import add_elements

class TestAddElements(unittest.TestCase):

    def test_add_elements(self):
        # Test case 1: Positive integers
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)

        # Test case 2: Negative integers
        self.assertEqual(add_elements([-111, -21, -3, 4000, -5, -6, -7, -8, -9], 4), -24)

        # Test case 3: Zero
        self.assertEqual(add_elements([0, 0, 0, 0, 0], 5), 0)

        # Test case 4: k greater than array length
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 10), 24)

        # Test case 5: k equal to array length
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 9), 24)

        # Test case 6: k less than 2
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 1), 3)

        # Test case 7: k equal to 1
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 1), 3)

        # Test case 8: k greater than 100
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 101), 24)

        # Test case 9: k equal to 100
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 100), 24)

        # Test case 10: k less than 1
        with self.assertRaises(ValueError):
            add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 0)

if __name__ == '__main__':
    unittest.main()


This script includes 10 test cases to cover different scenarios, including positive integers, negative integers, zero, k greater than array length, k equal to array length, k less than 2, k equal to 1, k greater than 100, and k less than 1. The test cases cover various edge cases and ensure the function works correctly in different situations.