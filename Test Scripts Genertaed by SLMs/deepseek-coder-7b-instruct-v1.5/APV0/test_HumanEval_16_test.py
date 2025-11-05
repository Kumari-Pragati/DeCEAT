You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_16_code import count_distinct_characters
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    return len(set(string.lower()))


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):
    def test_count_distinct_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)
        self.assertEqual(count_distinct_characters(''), 0)
        self.assertEqual(count_distinct_characters('aA'), 2)
        self.assertEqual(count_distinct_characters('1234567890'), 10)
        self.assertEqual(count_distinct_characters('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), 52)

if __name__ == '__main__':
    unittest.main()


This script creates a unittest.TestCase subclass with a single method, test_count_distinct_characters, which tests the count_distinct_characters function with a variety of inputs. The assertEqual method is used to check that the function's output matches the expected output.

The script ends with a call to unittest.main(), which runs all the tests when the script is run directly.

Please note that the HumanEval_16_code module should contain the count_distinct_characters function for these tests to work.