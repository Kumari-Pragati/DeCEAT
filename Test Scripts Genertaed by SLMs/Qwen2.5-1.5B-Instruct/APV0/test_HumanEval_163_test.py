system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_163_code import generate_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))
    return [i for i in range(lower, upper + 1) if i % 2 == 0]


assistant

import unittest

# Function to be tested
from HumanEval_163_code import generate_integers

class TestGenerateIntegers(unittest.TestCase):
    def test_generate_integers(self):
        # Test cases covering different scenarios
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 14), [])
        self.assertEqual(generate_integers(5, 7), [6])
        self.assertEqual(generate_integers(9, 9), [])

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a test case class `TestGenerateIntegers` that inherits from `unittest.TestCase`. It includes several test methods (`test_generate_integers`) to verify the correctness of the `generate_integers` function across various inputs. The `assertEqual` method is used to compare the output of the function against expected results. Finally, the `unittest.main()` call at the end makes the tests executable when run as a standalone script.