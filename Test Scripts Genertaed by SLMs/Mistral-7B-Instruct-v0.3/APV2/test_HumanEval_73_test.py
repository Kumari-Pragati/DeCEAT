You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_73_code import smallest_change
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
        smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
        smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
        smallest_change([1, 2, 3, 2, 1]) == 0
    """
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans

 Here is a complete unittest test suite for the `smallest_change` function:


import unittest
from HumanEval_73_code import smallest_change

class TestSmallestChange(unittest.TestCase):

    def test_smallest_change(self):
        self.assertEqual(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]), 4)
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)
        self.assertEqual(smallest_change([2, 2, 2, 2, 2]), 0)
        self.assertEqual(smallest_change([1, 1, 1, 1, 1]), 0)
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9]), 9)
        self.assertEqual(smallest_change([10, 20, 30, 40, 50, 60, 70, 80, 90]), 18)
        self.assertEqual(smallest_change([1, 1, 1, 0, 0, 0, 1, 1, 1]), 3)
        self.assertEqual(smallest_change([1, 1, 1, 1, 0, 0, 1, 1, 1]), 2)
        self.assertEqual(smallest_change([1, 1, 1, 1, 1, 0, 1, 1, 1]), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases for various inputs and edge cases. It uses the `assertEqual` method from the `unittest.TestCase` class to compare the expected output with the actual output of the `smallest_change` function. The test suite is run using the `unittest.main()` function at the end.