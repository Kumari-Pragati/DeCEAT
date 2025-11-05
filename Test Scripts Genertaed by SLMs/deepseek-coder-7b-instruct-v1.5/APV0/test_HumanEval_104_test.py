You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_104_code import unique_digits
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    odd_digit_elements = []
    for i in x:
        if all(int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_104_code import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_unique_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
        self.assertEqual(unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 5, 7, 9])
        self.assertEqual(unique_digits([11, 22, 33, 44, 55, 66, 77, 88, 99]), [])
        self.assertEqual(unique_digits([10, 20, 30, 40, 50, 60, 70, 80, 90]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestUniqueDigits` that inherits from `unittest.TestCase`. It defines a method `test_unique_digits` that tests the `unique_digits` function with various inputs and checks if the output matches the expected output.

The script ends with `if __name__ == '__main__': unittest.main()`, which means that the tests will be run when the script is executed directly.

Please note that you need to have the function `unique_digits` defined in the file `HumanEval_104_code.py` for this script to work.