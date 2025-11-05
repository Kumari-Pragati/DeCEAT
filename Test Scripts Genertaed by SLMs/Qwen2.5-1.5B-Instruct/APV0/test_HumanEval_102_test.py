system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_102_code import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num(self):
        # Test cases covering different scenarios
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(14, 16), 16)
        self.assertEqual(choose_num(17, 18), -1)
        self.assertEqual(choose_num(19, 18), -1)

        # Edge case where x equals y
        self.assertEqual(choose_num(10, 10), -1)

        # Edge case where x is greater than y
        self.assertEqual(choose_num(15, 12), -1)

if __name__ == '__main__':
    unittest.main()


Explanation of the code:

- The `unittest` module is imported at the beginning to set up the testing framework.
- The `TestChooseNum` class inherits from `unittest.TestCase`, which provides a base class for creating unit tests.
- The `test_choose_num` method contains several assertions using the `assertEqual` method to check the correctness of the `choose_num` function under various conditions.
- The `if __name__ == '__main__':` block ensures that when this file is executed as a standalone program, it runs all the tests defined in the `TestChooseNum` class.
- Each test case includes expected outcomes along with their corresponding input values to verify the functionality of the `choose_num` function.