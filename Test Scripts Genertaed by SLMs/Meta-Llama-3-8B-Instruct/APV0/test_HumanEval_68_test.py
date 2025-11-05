user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_68_code import pluck
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has the smallest index.

    The plucked node should be returned in a list, [smallest_value, its index].
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4, 2, 3]
        Output: [2, 1]

    Example 2:
        Input: [1, 2, 3]
        Output: [2, 1]

    Example 3:
        Input: []
        Output: []

    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
    if len(arr) == 0:
        return []
    evens = list(filter(lambda x: x % 2 == 0, arr))
    if evens == []:
        return []
    return [min(evens), arr.index(min(evens))]assistant

Here is the unittest test script for the `pluck` function:

import unittest
from HumanEval_68_code import pluck

class TestPluck(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(pluck([]), [])

    def test_no_even_values(self):
        self.assertEqual(pluck([1, 3, 5]), [])

    def test_single_even_value(self):
        self.assertEqual(pluck([2]), [2, 0])

    def test_multiple_even_values(self):
        self.assertEqual(pluck([2, 4, 6]), [2, 0])

    def test_multiple_even_values_with_smaller_index(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])

    def test_multiple_even_values_with_larger_index(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    def test_mixed_values(self):
        self.assertEqual(pluck([1, 2, 3, 4, 5]), [2, 1])

    def test_large_array(self):
        arr = [i for i in range(10000)]
        evens = [i for i in range(10000) if i % 2 == 0]
        self.assertEqual(pluck(arr), [min(evens), arr.index(min(evens))])

if __name__ == '__main__':
    unittest.main()

This test script covers a variety of scenarios, including:

* An empty array
* An array with no even values
* An array with a single even value
* An array with multiple even values
* An array with multiple even values, where the smallest index is not the smallest value
* An array with mixed values (both even and odd)
* A large array (10000 elements)

Each test case checks that the `pluck` function returns the expected result.