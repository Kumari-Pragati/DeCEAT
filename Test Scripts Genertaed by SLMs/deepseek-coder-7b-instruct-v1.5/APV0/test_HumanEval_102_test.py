You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_102_code import choose_num
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(12, 12), -1)
        self.assertEqual(choose_num(14, 16), 16)
        self.assertEqual(choose_num(16, 14), 14)
        self.assertEqual(choose_num(17, 17), -1)

if __name__ == '__main__':
    unittest.main()


This script tests the `choose_num` function with different input pairs. It checks if the function returns the correct output for each case.

Please note that you need to have the `HumanEval_102_code` module with the `choose_num` function defined in it for this script to work. If the function is not defined in a separate module, you can remove the import statement and define the function directly in the script.