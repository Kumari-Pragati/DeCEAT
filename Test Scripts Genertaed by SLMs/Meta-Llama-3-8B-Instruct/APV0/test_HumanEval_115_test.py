user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_115_code import max_fill
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    import math
    return sum([math.ceil(sum(arr) / capacity) for arr in grid])assistant

Here is a unittest test script for the `max_fill` function:

import unittest
from HumanEval_115_code import max_fill

class TestMaxFill(unittest.TestCase):
    def test_example1(self):
        grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 6)

    def test_example2(self):
        grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
        capacity = 2
        self.assertEqual(max_fill(grid, capacity), 5)

    def test_example3(self):
        grid = [[0, 0, 0], [0, 0, 0]]
        capacity = 5
        self.assertEqual(max_fill(grid, capacity), 0)

    def test_edge_cases(self):
        # Test with empty grid
        grid = []
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 0)

        # Test with single row
        grid = [[1, 1, 1, 1]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 4)

        # Test with varying capacities
        grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
        capacity = 3
        self.assertEqual(max_fill(grid, capacity), 2)

    def test_invalid_input(self):
        # Test with grid of wrong length
        grid = [[0, 0, 1, 0, 0]]
        capacity = 1
        with self.assertRaises(IndexError):
            max_fill(grid, capacity)

        # Test with capacity less than 1
        grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
        capacity = 0
        with self.assertRaises(ValueError):
            max_fill(grid, capacity)

if __name__ == '__main__':
    unittest.main()

This test script covers the following cases:

1. The three example inputs from the problem statement.
2. Edge cases, such as an empty grid, a single row, and varying capacities.
3. Invalid input cases, such as a grid of wrong length and a capacity less than 1.

Note that the `assertEqual` method is used to check that the output of the `max_fill` function matches the expected result, and the `assertRaises` method is used to check that the function raises the expected exception when given invalid input.