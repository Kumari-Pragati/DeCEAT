You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return sum([math.ceil(sum(arr) / capacity) for arr in grid])

 Here is the complete unittest test suite for the `max_fill` function:


import unittest
from HumanEval_115_code import max_fill

class TestMaxFill(unittest.TestCase):

    def test_example_1(self):
        grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
        capacity = 1
        expected_output = 6
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_example_2(self):
        grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
        capacity = 2
        expected_output = 5
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_example_3(self):
        grid = [[0, 0, 0], [0, 0, 0]]
        capacity = 5
        expected_output = 0
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_grid_size_constraints(self):
        grid = [[0] * 10001 for _ in range(10001)]
        capacity = 1
        with self.assertRaises(ValueError):
            max_fill(grid, capacity)

        grid = [[0, 0, 1, 1] for _ in range(10001)]
        capacity = 1
        with self.assertRaises(ValueError):
            max_fill(grid, capacity)

        grid = [[0, 0, 1, 1] for _ in range(10001)]
        capacity = 10001
        with self.assertRaises(ValueError):
            max_fill(grid, capacity)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases for the provided examples and an additional test case to check the grid size constraints. The `assertRaises` method is used to check if the function raises a `ValueError` when the grid size constraints are violated.