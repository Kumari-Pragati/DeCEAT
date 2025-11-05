You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_92_code import any_int
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    any_int(3, 2, 2) ➞ False
    any_int(3, -2, 1) ➞ True
    any_int(3.6, -2.2, 2) ➞ False
    '''

    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if (x + y == z) or (x + z == y) or (y + z == x):
            return True
        return False
    return False


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_92_code import any_int

class TestAnyInt(unittest.TestCase):
    def test_any_int(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertFalse(any_int(3, 2, 2))
        self.assertTrue(any_int(3, -2, 1))
        self.assertFalse(any_int(3.6, -2.2, 2))
        self.assertFalse(any_int(3, 2, 5))
        self.assertFalse(any_int(3, 2.2, 2))
        self.assertFalse(any_int(3, -2, 5.5))
        self.assertFalse(any_int(3.6, -2.2, 2.8))

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class TestAnyInt with a method test_any_int that tests the any_int function with different inputs. The assertTrue and assertFalse methods are used to assert that the function returns the correct output for each test case.

Please note that you need to replace `from HumanEval_92_code import any_int` with the actual location of your any_int function if it's not in the same file.

To run this script, you can simply execute it in your Python environment. If you're using a command line, you can do this by typing `python unittest_script.py` (replace `unittest_script.py` with the name of your script). If you're using an IDE, you can usually run the script by clicking on the run button.

The script will output the results of each test case to the console. If all tests pass, you'll see a message indicating that 0 tests failed of a total of 8 tests. If any tests fail, you'll see a message indicating how many tests failed and a list of the failing tests.