system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
        # Test case 1: List with no even numbers at odd indices
        self.assertEqual(add([4, 2, 6, 7]), 0)
        
        # Test case 2: List with one even number at an odd index
        self.assertEqual(add([4, 2, 6, 7, 8]), 2)

        # Test case 3: List with multiple even numbers at odd indices
        self.assertEqual(add([4, 2, 6, 7, 8, 9, 10]), 2)

        # Test case 4: Empty list (should raise ValueError)
        with self.assertRaises(ValueError):
            add([])

        # Test case 5: List with negative numbers (should work as expected)
        self.assertEqual(add([-4, -2, 6, 7, -8]), 2)

        # Test case 6: List with mixed values (should work as expected)
        self.assertEqual(add([4, 2, 6, 7, 8, 9, 10, 11, 12]), 2)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure the `add` function behaves correctly under various conditions, including edge cases like empty lists and lists containing negative numbers.