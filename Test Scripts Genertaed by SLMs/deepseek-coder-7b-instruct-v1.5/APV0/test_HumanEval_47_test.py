You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_47_code import median
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0


### Response:
Below is the unittest test script for the given Python function:


import unittest
from HumanEval_47_code import median

class TestMedian(unittest.TestCase):
    def test_odd_length(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_even_length(self):
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

    def test_single_element(self):
        self.assertEqual(median([1]), 1)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            median([])

    def test_duplicate_elements(self):
        self.assertEqual(median([1, 2, 2, 3, 4]), 2)

if __name__ == '__main__':
    unittest.main()


This script includes tests for odd-length lists, even-length lists, a list with a single element, an empty list, and a list with duplicate elements. It checks that the function returns the correct median for each of these cases. If any of these tests fail, the script will raise an AssertionError.

Please note that the function `median` should be defined in the file `HumanEval_47_code.py` for the test script to work.