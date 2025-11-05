You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_60_code import sum_to_n
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum(range(n + 1))


### Response:
Here is the unittest script for the given Python function:


import unittest
from HumanEval_60_code import sum_to_n

class TestSumToN(unittest.TestCase):
    def test_sum_to_n(self):
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(1), 1)

if __name__ == '__main__':
    unittest.main()


This script creates a test case class `TestSumToN` that inherits from `unittest.TestCase`. Inside this class, a test method `test_sum_to_n` is defined to test the `sum_to_n` function. The `assertEqual` method is used to check if the actual output of `sum_to_n` matches the expected output.

The script ends with `if __name__ == '__main__': unittest.main()`, which means the test case will be run when the script is executed directly.

Please note that you need to have the `HumanEval_60_code` module and the `sum_to_n` function defined in it to run this script.