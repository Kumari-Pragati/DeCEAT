You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_163_code import generate_integers

class TestGenerateIntegers(unittest.TestCase):

    def test_generate_integers(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 14), [])
        self.assertEqual(generate_integers(1, 1), [])
        self.assertEqual(generate_integers(9, 11), [])
        self.assertEqual(generate_integers(2, 8), generate_integers(8, 2))
        self.assertEqual(generate_integers(10, 14), generate_integers(14, 10))
        self.assertEqual(generate_integers(1, 1), generate_integers(1, 1))
        self.assertEqual(generate_integers(9, 11), generate_integers(11, 9))

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestGenerateIntegers` that inherits from `unittest.TestCase`. It includes a method `test_generate_integers` that tests the `generate_integers` function with various inputs. Each test case checks if the actual output matches the expected output.

The script ends with `if __name__ == '__main__': unittest.main()`, which runs the test cases when the script is run directly.

Please note that the `generate_integers` function is expected to be defined in a file named `HumanEval_163_code.py` and should be in the same directory as the unittest script.