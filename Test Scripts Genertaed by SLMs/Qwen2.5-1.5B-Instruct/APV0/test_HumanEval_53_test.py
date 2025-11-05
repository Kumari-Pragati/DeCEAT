system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_53_code import add
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y


assistant

import unittest

# Importing the function to be tested
from HumanEval_53_code import add

class TestAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()


This script imports the `unittest` module and the `add` function from your code. It then defines a class `TestAddition` that inherits from `unittest.TestCase`. Within this class, there is a method `test_add` which uses assertions (`self.assertEqual`) to check if the `add` function returns the correct results when given specific inputs. Finally, it calls `unittest.main()` to run all tests in the `TestAddition` class.