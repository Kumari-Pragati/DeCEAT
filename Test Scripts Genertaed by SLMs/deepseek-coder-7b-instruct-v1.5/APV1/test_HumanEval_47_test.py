You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_47_code import median

class TestMedian(unittest.TestCase):
    def test_odd_length(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(median([10, 20, 30, 40, 50, 60]), 35)

    def test_even_length(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(median([10, 20, 30, 40]), 25)

    def test_single_element(self):
        self.assertEqual(median([1]), 1)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            median([])

    def test_negative_numbers(self):
        self.assertEqual(median([-1, -2, -3, -4, -5]), -3)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for lists of odd and even lengths, a list with a single element, and an empty list. It also includes a test for negative numbers.

Please note that the `median` function in your code does not handle an empty list. If you want to handle this case, you should add a check for an empty list at the beginning of your function and raise an appropriate exception.