system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

# Importing the function to be tested
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

        # Test case 5: Mixed types (should work as long as all elements are of type int)
        self.assertEqual(unique([1, 'a', 2, 'b']), ['a', 1, 'b', 2])

if __name__ == '__main__':
    unittest.main()


This script defines a `TestUnique` class that inherits from `unittest.TestCase`. It contains several test cases to ensure the `unique` function behaves correctly under various conditions. The `test_unique` method is used to verify the correctness of the function using assertions. Finally, the `if __name__ == '__main__':` block runs the tests when the script is executed directly.