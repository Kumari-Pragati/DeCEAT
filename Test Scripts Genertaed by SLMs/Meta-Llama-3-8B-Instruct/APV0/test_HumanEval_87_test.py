user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_87_code import get_row
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_row(lst, x):
    """
    You are given a 2 dimensional data, as nested lists,
    which is similar to a matrix; however, unlike matrices,
    each row may contain a different number of columns.
    Given lst and integer x, find occurrences of x in the list,
    and return a list of tuples [(x1, y1), (x2, y2)...] such that
    each tuple is a coordinate - (row, column), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1, 2, 3, 4, 5, 6],
      [1, 2, 3, 4, 1, 6],
      [1, 2, 3, 4, 5, 1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """

    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])assistant

Here is the unittest test script for the `get_row` function:

import unittest
from HumanEval_87_code import get_row

class TestGetRow(unittest.TestCase):
    def test_example1(self):
        lst = [[1, 2, 3, 4, 5, 6],
              [1, 2, 3, 4, 1, 6],
              [1, 2, 3, 4, 5, 1]]
        self.assertEqual(get_row(lst, 1), [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)])

    def test_empty_list(self):
        self.assertEqual(get_row([], 1), [])

    def test_single_row(self):
        lst = [[1, 2, 3, 4, 5, 6]]
        self.assertEqual(get_row(lst, 3), [(0, 2)])

    def test_multiple_rows(self):
        lst = [[1, 2, 3, 4, 5, 6],
              [1, 2, 3, 4, 1, 6],
              [1, 2, 3, 4, 5, 1]]
        self.assertEqual(get_row(lst, 3), [])

    def test_nested_lists(self):
        lst = [[], [1], [1, 2, 3]]
        self.assertEqual(get_row(lst, 3), [(2, 2)])

    def test_no_occurrences(self):
        lst = [[1, 2, 3, 4, 5, 6],
              [1, 2, 3, 4, 1, 6],
              [1, 2, 3, 4, 5, 1]]
        self.assertEqual(get_row(lst, 7), [])

if __name__ == '__main__':
    unittest.main()

This test script covers the following scenarios:

1. The example provided in the problem statement.
2. An empty list.
3. A single row with occurrences of the target value.
4. Multiple rows with occurrences of the target value.
5. A nested list with occurrences of the target value.
6. A list with no occurrences of the target value.

Each test method checks the output of the `get_row` function against the expected result using the `assertEqual` method.