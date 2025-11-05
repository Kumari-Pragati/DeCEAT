system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_44_code import change_base
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret


assistant

import unittest

# Importing the function to be tested
from HumanEval_44_code import change_base


class TestChangeBase(unittest.TestCase):

    def test_change_base(self):
        self.assertEqual(change_base(8, 3), "22")
        self.assertEqual(change_base(8, 2), "1000")
        self.assertEqual(change_base(7, 2), "111")

    def test_edge_cases(self):
        # Testing edge cases where x or base could cause issues (e.g., division by zero)
        self.assertRaises(ValueError, change_base, -1, 2)
        self.assertRaises(ValueError, change_base, 5, 0)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `unittest` test case class `TestChangeBase` that includes two test methods:

1. `test_change_base`: This method tests the functionality of the `change_base` function using predefined inputs and expected outputs. It uses assertions to check if the output matches the expected results.

2. `test_edge_cases`: This method checks for potential errors in the function's behavior under specific conditions. For example, it tests what happens when the input number is negative (`-1`) or the target base is zero (`0`). The `assertRaises` method is used to verify that these scenarios raise appropriate exceptions as expected.

The `unittest.main()` call at the end runs all the defined test methods.