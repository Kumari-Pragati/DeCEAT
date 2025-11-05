user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_90_code import next_smallest
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """

    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]assistant

Here is the unittest test script for the `next_smallest` function:

import unittest
from HumanEval_90_code import next_smallest

class TestNextSmallest(unittest.TestCase):
    def test_next_smallest(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)
        self.assertIsNone(next_smallest([]))
        self.assertIsNone(next_smallest([1, 1]))
        self.assertEqual(next_smallest([1, 2, 3, 4, 5, 6]), 2)
        self.assertEqual(next_smallest([1, 3, 2, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 4, 3, 2, 1]), 2)
        self.assertEqual(next_smallest([1, 1, 2, 3, 4, 5]), None)

if __name__ == '__main__':
    unittest.main()

This test script includes 7 test cases to cover various scenarios:

1. A list with a single smallest element.
2. A list with multiple smallest elements.
3. An empty list.
4. A list with duplicate smallest elements.
5. A list with multiple smallest elements and a larger element.
6. A list with multiple smallest elements and a smaller element.
7. A list with multiple smallest elements and a duplicate smallest element.

The `assertEqual` method is used to check if the output of the `next_smallest` function matches the expected result. The `assertNone` method is used to check if the output is `None` as expected.