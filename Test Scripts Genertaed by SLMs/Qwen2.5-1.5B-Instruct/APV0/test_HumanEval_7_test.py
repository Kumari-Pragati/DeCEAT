system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Define the function to be tested
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):
    def test_filter_by_substring(self):
        # Test case 1: Empty input
        self.assertEqual(filter_by_substring([], "test"), [])

        # Test case 2: Single string input
        self.assertEqual(filter_by_substring(["hello"], "l"), ["hello"])

        # Test case 3: Multiple strings containing the substring
        self.assertEqual(
            filter_by_substring(["apple", "banana", "cherry", "date"], "a"),
            ["apple", "banana"]
        )

        # Test case 4: Multiple strings not containing the substring
        self.assertEqual(
            filter_by_substring(["orange", "grapefruit", "kiwi"], "b"),
            []
        )

        # Test case 5: String with multiple substrings
        self.assertEqual(
            filter_by_substring(["sunflower", "daisy", "rose", "tulip"], "da"),
            ["daisy", "rose"]
        )

        # Test case 6: Substring is an empty string
        self.assertEqual(
            filter_by_substring(["cat", "dog", "elephant"], ""),
            []
        )

        # Test case 7: Substring is longer than any string in the list
        self.assertEqual(
            filter_by_substring(["short", "longer", "verylong"], "very"),
            ["verylong"]
        )

if __name__ == '__main__':
    unittest.main()


This script defines a unit test class `TestFilterBySubstring` that inherits from `unittest.TestCase`. It contains several test cases to verify the functionality of the `filter_by_substring` function. The `assertEqual` method is used to check if the output of the function matches the expected result. Finally, the `unittest.main()` call runs all the tests when the script is executed.