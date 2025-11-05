Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_42_code import incr_list
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [e + 1 for e in l]

 import unittest
from HumanEval_42_code import incr_list

class TestIncrList(unittest.TestCase):

    def test_increment_list(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])
        self.assertEqual(incr_list([]), [])
        self.assertEqual(incr_list([0]), [1])
        self.assertEqual(incr_list([-1]), [0])
        self.assertEqual(incr_list([100]), [101])
        self.assertEqual(incr_list([100, 200]), [101, 201])
        self.assertEqual(incr_list([-100, -200]), [-99, -199])

    def test_increment_empty_list(self):
        self.assertEqual(incr_list([]), [])

    def test_increment_single_element(self):
        self.assertEqual(incr_list([0]), [1])
        self.assertEqual(incr_list([-1]), [0])
        self.assertEqual(incr_list([100]), [101])
        self.assertEqual(incr_list([-100]), [-99])

    def test_increment_mixed_elements(self):
        self.assertEqual(incr_list([1, -2, 3, -4, 5]), [2, -1, 4, -3, 6])

if __name__ == '__main__':
    unittest.main()