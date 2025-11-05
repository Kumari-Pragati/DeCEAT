You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_115_code import max_fill

class TestMaxFill(unittest.TestCase):

    def test_empty_grid(self):
        grid = [[0, 0, 0], [0, 0, 0]]
        capacity = 5
        expected_output = 0
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_single_well(self):
        grid = [[1]]
        capacity = 1
        expected_output = 1
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_multiple_wells_same_capacity(self):
        grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
        capacity = 1
        expected_output = 6
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_multiple_wells_different_capacity(self):
        grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
        capacity = 2
        expected_output = 5
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_large_grid(self):
        grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
        capacity = 1
        expected_output = 1
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_large_grid_with_multiple_wells(self):
        grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
        capacity = 2
        expected_output = 1
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_edge_case_empty_grid_with_capacity(self):
        grid = []
        capacity = 1
        expected_output = 0
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_edge_case_single_well_with_capacity(self):
        grid = [[1]]
        capacity = 1
        expected_output = 1
        self.assertEqual(max_fill(grid, capacity), expected_output)

    def test_edge_case_large_grid_with_capacity(self):
        grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
        capacity = 1
        expected_output = 1
        self.assertEqual(max_fill(grid, capacity), expected_output)

if __name__ == '__main__':
    unittest.main()