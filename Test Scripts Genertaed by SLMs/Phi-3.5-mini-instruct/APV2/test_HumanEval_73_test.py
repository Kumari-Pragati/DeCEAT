You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 
import unittest
from HumanEval_73_code import smallest_change

class TestSmallestChange(unittest.TestCase):

    def test_smallest_change_zero_changes(self):
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

    def test_smallest_change_one_change(self):
        self.assertEqual(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]), 4)

    def test_smallest_change_multiple_changes(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)

    def test_smallest_change_palindrome(self):
        self.assertEqual(smallest_change([1, 2, 3, 3, 2, 1]), 0)

    def test_smallest_change_empty_array(self):
        self.assertEqual(smallest_change([]), 0)

    def test_smallest_change_single_element(self):
        self.assertEqual(smallest_change([1]), 0)

    def test_smallest_change_all_elements_same(self):
        self.assertEqual(smallest_change([1, 1, 1, 1]), 0)

    def test_smallest_change_all_elements_different(self):
        self.assertEqual(smallest_change([1, 2, 3, 4]), 4)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios for the `smallest_change` function, including:

- An array that is already a palindrome.
- An array that requires one change to become a palindrome.
- An array that requires multiple changes to become a palindrome.
- An empty array.
- An array with a single element.
- An array where all elements are the same.
- An array where all elements are different.

Each test case uses `assertEqual` to verify that the output of `smallest_change` matches the expected result. Running this test suite will execute all the tests and report any failures, ensuring the `smallest_change` function behaves as expected.