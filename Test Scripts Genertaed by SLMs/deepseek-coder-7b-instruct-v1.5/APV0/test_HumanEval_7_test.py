You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_7_code import filter_by_substring
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter the list of strings and return only those that contain `substring`.
    >>> filter_by_substring(['abc', 'def', 'ab'], 'ab')
    ['abc', 'ab']
    """
    return [x for x in strings if substring in x]


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):
    def test_filter_by_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'cd'), [])
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], ''), ['abc', 'def', 'ab'])
        self.assertEqual(filter_by_substring([], 'ab'), [])
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'a'), ['abc', 'ab'])
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'b'), ['abc', 'ab'])
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'c'), ['abc'])
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'd'), [])
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'e'), [])
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'f'), [])

if __name__ == '__main__':
    unittest.main()


This script creates a subclass of `unittest.TestCase` and defines a method `test_filter_by_substring` that tests the `filter_by_substring` function with various inputs. Each test case checks that the function returns the expected output for a given input.

The `unittest.main()` at the end of the script runs the tests when the script is run directly.