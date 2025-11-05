system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_42_code import incr_list
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [e + 1 for e in l]


assistant

import unittest

# Importing the function to be tested
from HumanEval_42_code import incr_list

class TestIncrList(unittest.TestCase):

    def test_incr_list(self):
        # Test case 1
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4], "Test case 1 failed")

        # Test case 2
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), 
                         [6, 4, 6, 3, 4, 4, 10, 1, 124], 
                         "Test case 2 failed")

        # Test case 3 (empty list)
        self.assertEqual(incr_list([]), [], "Test case 3 failed")

        # Test case 4 (single element list)
        self.assertEqual(incr_list([7]), [8], "Test case 4 failed")

        print("All tests passed!")

if __name__ == '__main__':
    unittest.main()


This script imports the `unittest` module and the `incr_list` function from another file named `HumanEval_42_code`. It then defines a class `TestIncrList` that inherits from `unittest.TestCase`, which allows you to write test cases using methods starting with `test_`.

Each test case is defined within its own method, where it calls the `incr_list` function with different inputs and compares the output against expected results using the `assertEqual` method of `unittest.TestCase`. If any test fails, an assertion error will be raised, indicating which test failed.

Finally, if this script is run as the main program (`if __name__ == '__main__':`), it will execute all the test cases and print "All tests passed!" if they all pass successfully.