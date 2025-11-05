You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_76_code import is_simple_power

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int = x
    For example:
        is_simple_power(1, 4) => True
        is_simple_power(2, 2) => True
        is_simple_power(8, 2) => True
        is_simple_power(3, 2) => False
        is_simple_power(3, 1) => False
        is_simple_power(5, 3) => False
    """

    if n == 1:
        return x == 1

    power = 1
    while power < x:
        power *= n

    return power == x


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_76_code import is_simple_power

class TestIsSimplePower(unittest.TestCase):
    def test_simple_power(self):
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))

if __name__ == '__main__':
    unittest.main()


This test suite includes a single test case `test_simple_power` that tests the `is_simple_power` function with a variety of inputs. The `assertTrue` and `assertFalse` methods are used to check that the function returns the correct output for each test case.

Please note that the `HumanEval_76_code` module should contain the `is_simple_power` function for these tests to work. If the function is defined in a different module, you should replace `from HumanEval_76_code import is_simple_power` with the appropriate import statement.