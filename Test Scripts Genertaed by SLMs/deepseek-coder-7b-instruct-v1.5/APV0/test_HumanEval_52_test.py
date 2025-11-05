You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_52_code import below_threshold
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for e in l:
        if e >= t:
            return False
    return True


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_52_code import below_threshold

class TestBelowThreshold(unittest.TestCase):

    def test_all_below(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))

    def test_one_above(self):
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

    def test_empty_list(self):
        self.assertTrue(below_threshold([], 100))

    def test_all_above(self):
        self.assertFalse(below_threshold([101, 202, 404, 1000], 100))

    def test_negative_numbers(self):
        self.assertFalse(below_threshold([-1, -2, -4, -10], 0))

if __name__ == '__main__':
    unittest.main()


This script creates a unittest.TestCase subclass with several test methods. Each method tests a different scenario. The `test_all_below` method tests when all numbers in the list are below the threshold, `test_one_above` tests when one number in the list is above the threshold, `test_empty_list` tests when the list is empty, `test_all_above` tests when all numbers in the list are above the threshold, and `test_negative_numbers` tests when the list contains negative numbers.

To run these tests, you would need to have the `HumanEval_52_code` module available, and it would need to contain the `below_threshold` function.