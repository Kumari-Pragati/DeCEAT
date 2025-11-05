system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_7_code import filter_by_substring
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

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


assistant

import unittest

# Importing the function from the given context
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):
    def test_normal_input(self):
        result = filter_by_substring(['abc', 'def', 'ab', 'ghij'], 'ab')
        expected = ['abc', 'ab']
        self.assertListEqual(result, expected)

    def test_edge_case_with_single_element(self):
        result = filter_by_substring(['single'], 'any')
        expected = ['single']
        self.assertListEqual(result, expected)

    def test_edge_case_with_no_match(self):
        result = filter_by_substring(['no match here'], 'anything')
        expected = []
        self.assertListEqual(result, expected)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            filter_by_substring(123, 'test')

if __name__ == '__main__':
    unittest.main()