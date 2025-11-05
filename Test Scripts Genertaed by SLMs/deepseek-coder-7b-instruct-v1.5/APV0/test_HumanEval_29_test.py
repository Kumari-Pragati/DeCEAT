You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_29_code import filter_by_prefix
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [x for x in strings if x.startswith(prefix)]


### Response:
Here is the unittest script for the given Python function:


import unittest
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z'), [])

    def test_single_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_multiple_prefixes(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array', 'apple'], 'a'), ['abc', 'array', 'apple'])

    def test_case_sensitivity(self):
        self.assertEqual(filter_by_prefix(['Abc', 'Bcd', 'Cde', 'Array'], 'a'), [])

if __name__ == '__main__':
    unittest.main()


This script tests the `filter_by_prefix` function with various scenarios:

1. An empty list and a prefix.
2. A list with no strings starting with the prefix.
3. A list with a single string starting with the prefix.
4. A list with multiple strings starting with the prefix.
5. Case sensitivity: a list with strings starting with the prefix but in different cases.

Please note that the `HumanEval_29_code` module should contain the `filter_by_prefix` function for these tests to work.