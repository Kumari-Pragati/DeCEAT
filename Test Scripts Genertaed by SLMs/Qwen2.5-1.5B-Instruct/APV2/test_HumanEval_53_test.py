system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

# Provided function
from HumanEval_53_code import add

class TestAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()


This test suite includes a `TestAddition` class that inherits from `unittest.TestCase`. It contains a single method `test_add`, which uses assertions to verify that the `add` function returns the correct results for given inputs. The `assertEqual` method checks if the actual result of calling `add` with specific arguments matches the expected value. If any assertion fails, it will raise an error indicating which test failed.