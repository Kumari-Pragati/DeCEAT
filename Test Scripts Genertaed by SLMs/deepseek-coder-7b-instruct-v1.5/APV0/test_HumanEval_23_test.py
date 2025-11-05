You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_23_code import strlen
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_23_code import strlen

class TestStrlen(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)

    def test_string_with_spaces(self):
        self.assertEqual(strlen('hello world'), 10)

    def test_string_with_special_characters(self):
        self.assertEqual(strlen('hello@world'), 10)

    def test_string_with_numbers(self):
        self.assertEqual(strlen('1234567890'), 10)

if __name__ == '__main__':
    unittest.main()


This script creates a unittest test case for the strlen function. It tests the function with empty string, non-empty string, string with spaces, string with special characters, and string with numbers.

Please replace `HumanEval_23_code` with the actual module name where strlen function is defined.

To run this script, you need to have Python's unittest module installed. If you don't have it, you can install it using pip:

bash
pip install unittest


Then you can run the script using Python:

bash
python test_strlen.py


Replace `test_strlen.py` with the actual name of your test script.