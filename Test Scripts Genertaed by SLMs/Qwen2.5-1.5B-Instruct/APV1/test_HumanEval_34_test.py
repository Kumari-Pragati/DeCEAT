system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_34_code import unique
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))


assistant

import unittest

# Function to be tested
from HumanEval_34_code import unique

class TestUnique(unittest.TestCase):

    def test_unique(self):
        # Test case 1: Basic usage
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

        # Test case 2: Empty list
        self.assertEqual(unique([]), [])

        # Test case 3: Single element list
        self.assertEqual(unique([7]), [7])

        # Test case 4: List with duplicate elements
        self.assertEqual(unique([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

        # Test case 5: Mixed types (should work as long as all elements are of the same type)
        self.assertEqual(unique(['a', 'b', 'c']), ['a', 'b', 'c'])

        print("All tests passed!")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestUnique` class that inherits from `unittest.TestCase`. It contains several test cases using the `assertEqual` method to verify that the output of the `unique` function matches the expected results. The `unittest.main()` call at the end runs these tests when the script is executed directly.