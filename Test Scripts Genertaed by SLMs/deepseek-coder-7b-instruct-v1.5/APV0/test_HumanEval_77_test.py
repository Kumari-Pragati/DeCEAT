You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_77_code import iscube
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
        iscube(1) ==> True
        iscube(2) ==> False
        iscube(-1) ==> True
        iscube(64) ==> True
        iscube(0) ==> True
        iscube(180) ==> False
    '''

    a = abs(a)
    return int(round(a ** (1.0 / 3))) ** 3 == a


### Response:
Here is the unittest script for the given Python function:


import unittest
from HumanEval_77_code import iscube

class TestIscube(unittest.TestCase):

    def test_iscube_positive(self):
        self.assertTrue(iscube(1))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(0))

    def test_iscube_negative(self):
        self.assertTrue(iscube(-1))
        self.assertFalse(iscube(2))
        self.assertFalse(iscube(180))

    def test_iscube_large_numbers(self):
        self.assertTrue(iscube(12167))
        self.assertFalse(iscube(12168))

if __name__ == '__main__':
    unittest.main()


This script includes three test methods:

- `test_iscube_positive`: tests the function with positive numbers.
- `test_iscube_negative`: tests the function with negative numbers.
- `test_iscube_large_numbers`: tests the function with large numbers.

Each method checks if the function returns the correct output for a given input. The `assertTrue` function is used when the expected output is True, and `assertFalse` is used when the expected output is False.

Please note that the `HumanEval_77_code` module should contain the `iscube` function for these tests to work. If the function is defined in a different module, you should replace `HumanEval_77_code` with the correct module name.