You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_35_code import max_element
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):
    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)
        self.assertEqual(max_element([-1, -2, -3]), -1)
        self.assertEqual(max_element([1]), 1)
        self.assertEqual(max_element([]), None)
        self.assertIsNone(max_element([]))

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure that the `max_element` function works correctly. The `assertEqual` method is used to check that the function's output matches the expected output. The `assertIsNone` method is used to check that the function returns `None` when given an empty list.

Please note that you need to have the `HumanEval_35_code` module and the `max_element` function defined in it for this script to work. If the function is defined in a different module, you should replace `HumanEval_35_code` with the correct module name.