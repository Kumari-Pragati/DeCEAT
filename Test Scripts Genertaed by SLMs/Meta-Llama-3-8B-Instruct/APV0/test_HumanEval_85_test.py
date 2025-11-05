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

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_85_code import add

class TestAddFunction(unittest.TestCase):

    def test_add_function(self):
        # Test case 1: Positive integers
        self.assertEqual(add([4, 2, 6, 7]), 2)

        # Test case 2: Negative integers
        self.assertEqual(add([-4, -2, -6, 7]), -2)

        # Test case 3: Zero
        self.assertEqual(add([0, 2, 6, 7]), 0)

        # Test case 4: Empty list
        with self.assertRaises(IndexError):
            add([])

        # Test case 5: List with no even elements at odd indices
        self.assertEqual(add([1, 3, 5, 7]), 0)

        # Test case 6: List with multiple even elements at odd indices
        self.assertEqual(add([4, 2, 6, 8, 10]), 6)

        # Test case 7: List with negative even elements at odd indices
        self.assertEqual(add([-4, -2, -6, -8, -10]), -4)

if __name__ == '__main__':
    unittest.main()


This script includes seven test cases to cover different scenarios, including positive and negative integers, zero, empty list, and lists with multiple even elements at odd indices. The `assertEqual` method is used to check if the output of the function matches the expected result, and the `assertRaises` method is used to check if the function raises an `IndexError` when an empty list is passed.