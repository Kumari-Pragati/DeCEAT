You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    and return a list of tuples [(x1, y1), (x2, y2) ...] such that
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
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_87_code import get_row

class TestGetRow(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_row([], 1), [])

    def test_single_element_list(self):
        self.assertEqual(get_row([[1]], 1), [(0, 0)])
        self.assertEqual(get_row([[2]], 1), [])

    def test_multiple_elements_list(self):
        self.assertEqual(get_row([[1, 2, 3], [4, 5, 1]], 1), [(0, 0), (1, 2)])
        self.assertEqual(get_row([[1, 2, 3], [4, 5, 6]], 6), [(1, 2)])
        self.assertEqual(get_row([[1, 2, 3], [4, 5, 6]], 7), [])

    def test_different_row_lengths(self):
        self.assertEqual(get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1), [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)])
        self.assertEqual(get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], []], 1), [(0, 0), (1, 4), (1, 0)])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for empty lists, lists with single elements, lists with multiple elements, and lists with different row lengths. It tests the function with different values of x and checks if the output is as expected.