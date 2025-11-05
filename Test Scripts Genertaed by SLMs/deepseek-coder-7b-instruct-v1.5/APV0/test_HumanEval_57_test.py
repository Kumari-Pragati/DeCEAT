You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_57_code import monotonic
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):

    def test_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))

    def test_decreasing(self):
        self.assertTrue(monotonic([4, 1, 0, -10]))

    def test_mixed(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))

    def test_equal(self):
        self.assertTrue(monotonic([1, 1, 1, 1]))

    def test_empty(self):
        self.assertTrue(monotonic([]))

    def test_single(self):
        self.assertTrue(monotonic([1]))

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestMonotonic` that inherits from `unittest.TestCase`. It includes several test methods, each testing a different scenario. The `assertTrue` method is used to check if the function returns the expected result.

Please note that you need to replace `from HumanEval_57_code import monotonic` with the actual location of your `monotonic` function. If your function is in a different file or module, you need to adjust the import statement accordingly.

To run the tests, you can simply execute this script. The `unittest.main()` call at the end will run all the test methods in the `TestMonotonic` class.