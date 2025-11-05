You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(12, 12), -1)
        self.assertEqual(choose_num(15, 12), -1)
        self.assertEqual(choose_num(14, 16), 16)
        self.assertEqual(choose_num(16, 14), 14)
        self.assertEqual(choose_num(17, 17), -1)
        self.assertEqual(choose_num(18, 20), 20)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- When the first number is greater than the second number, the function should return -1.
- When the second number is even, the function should return the second number.
- When the first and second number are the same and are odd, the function should return -1.
- When the second number is one less than the first number and both are odd, the function should return the first number minus one.
- When the second number is even and greater than the first number, the function should return the second number.
- When the first number is even and greater than the second number, the function should return the first number minus one.
- When both numbers are odd and the same, the function should return -1.
- When both numbers are even and the second number is greater than the first, the function should return the second number.
- When both numbers are even and the first number is greater than the second, the function should return the first number minus one.

This test suite should cover all the possible scenarios for the given function.