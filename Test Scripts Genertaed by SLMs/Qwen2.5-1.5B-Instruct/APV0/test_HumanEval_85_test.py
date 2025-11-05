system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_85_code import add
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(lst):
    """Given a non-empty list of integers lst. Add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])


assistant

import unittest

# Function to be tested
from HumanEval_85_code import add

class TestAdd(unittest.TestCase):

    def test_add(self):
        # Test case 1: List with only one element (even)
        self.assertEqual(add([4]), 4)

        # Test case 2: List with two elements (one is even)
        self.assertEqual(add([4, 2]), 2)

        # Test case 3: List with three elements (two are even)
        self.assertEqual(add([4, 2, 6]), 2)

        # Test case 4: List with four elements (three are even)
        self.assertEqual(add([4, 2, 6, 7]), 2)

        # Test case 5: List with five elements (four are even)
        self.assertEqual(add([4, 2, 6, 7, 8]), 2)

        # Test case 6: List with six elements (five are even)
        self.assertEqual(add([4, 2, 6, 7, 8, 9]), 2)

        # Test case 7: List with seven elements (six are even)
        self.assertEqual(add([4, 2, 6, 7, 8, 9, 10]), 2)

        # Test case 8: List with eight elements (seven are even)
        self.assertEqual(add([4, 2, 6, 7, 8, 9, 10, 11]), 2)

        # Test case 9: List with nine elements (eight are even)
        self.assertEqual(add([4, 2, 6, 7, 8, 9, 10, 11, 12]), 2)

        # Test case 10: List with ten elements (nine are even)
        self.assertEqual(add([4, 2, 6, 7, 8, 9, 10, 11, 12, 13]), 2)

if __name__ == '__main__':
    unittest.main()


This script defines a `TestAdd` class within the `unittest` module, which contains a single test method `test_add`. Each test case checks various scenarios to ensure the `add` function behaves as expected. The `unittest.main()` call at the end makes the tests executable when run directly.