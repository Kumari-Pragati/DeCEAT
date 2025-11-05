You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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
    return sum([math.ceil(sum(arr) / capacity) for arr in grid])


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_115_code import max_fill

class TestMaxFill(unittest.TestCase):

    def test_max_fill(self):
        # Test case 1
        grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 6)

        # Test case 2
        grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
        capacity = 2
        self.assertEqual(max_fill(grid, capacity), 5)

        # Test case 3
        grid = [[0,0,0], [0,0,0]]
        capacity = 5
        self.assertEqual(max_fill(grid, capacity), 0)

        # Test case 4
        grid = [[1,1,1,1,1], [1,1,1,1,1]]
        capacity = 3
        self.assertEqual(max_fill(grid, capacity), 3)

        # Test case 5
        grid = [[0,1,0,1,0], [1,0,1,0,1]]
        capacity = 2
        self.assertEqual(max_fill(grid, capacity), 4)

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class TestMaxFill with a method test_max_fill. This method contains multiple test cases to fully test the max_fill function. Each test case checks if the output of the function matches the expected output.

To run this script, you need to have the HumanEval_115_code.py file in the same directory or adjust the import statement accordingly.

Please note that the unittest module is a built-in Python library for testing, and it provides a rich set of tools for constructing and running tests.