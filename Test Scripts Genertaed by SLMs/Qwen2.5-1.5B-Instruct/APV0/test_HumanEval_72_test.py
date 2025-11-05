system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_72_code import will_it_fly
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def will_it_fly(q, w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements
    is less than or equal to the maximum possible weight w.

    Example:
        will_it_fly([1, 2], 5) ➞ False 
        # 1+2 is less than the maximum possible weight, but it's unbalanced.

        will_it_fly([3, 2, 3], 1) ➞ False
        # it's balanced, but 3+2+3 is more than the maximum possible weight.

        will_it_fly([3, 2, 3], 9) ➞ True
        # 3+2+3 is less than the maximum possible weight, and it's balanced.

        will_it_fly([3], 5) ➞ True
        # 3 is less than the maximum possible weight, and it's balanced.
    '''
    if sum(q) > w:
        return False

    i, j = 0, len(q) - 1
    while i < j:
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1
    return True


assistant

import unittest

# Importing the function we want to test
from HumanEval_72_code import will_it_fly

class TestWillItFly(unittest.TestCase):
    def test_will_it_fly(self):
        self.assertEqual(will_it_fly([1, 2], 5), False)
        self.assertEqual(will_it_fly([3, 2, 3], 1), False)
        self.assertEqual(will_it_fly([3, 2, 3], 9), True)
        self.assertEqual(will_it_fly([3], 5), True)

if __name__ == '__main__':
    unittest.main()


This script imports the `will_it_fly` function from the `HumanEval_72_code` module and defines a class `TestWillItFly` within the `unittest` framework. It contains four test cases using the `assertEqual` method to verify the correctness of the `will_it_fly` function against provided data points. Finally, the `if __name__ == '__main__':` block runs all tests when the script is executed directly.