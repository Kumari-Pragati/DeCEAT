system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])assistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_85_code import add

class TestAddFunction(unittest.TestCase):

    def test_add_function(self):
        # Test case 1: add([4, 2, 6, 7]) == 2
        self.assertEqual(add([4, 2, 6, 7]), 2)

        # Test case 2: add([1, 3, 5, 7]) == 0
        self.assertEqual(add([1, 3, 5, 7]), 0)

        # Test case 3: add([2, 4, 6, 8]) == 6
        self.assertEqual(add([2, 4, 6, 8]), 6)

        # Test case 4: add([1, 2, 3, 4]) == 2
        self.assertEqual(add([1, 2, 3, 4]), 2)

        # Test case 5: add([5, 6, 7, 8]) == 4
        self.assertEqual(add([5, 6, 7, 8]), 4)

        # Test case 6: add([1, 3, 5, 7, 9]) == 0
        self.assertEqual(add([1, 3, 5, 7, 9]), 0)

        # Test case 7: add([2, 4, 6, 8, 10]) == 10
        self.assertEqual(add([2, 4, 6, 8, 10]), 10)

        # Test case 8: add([1, 2, 3, 4, 5]) == 2
        self.assertEqual(add([1, 2, 3, 4, 5]), 2)

        # Test case 9: add([6, 7, 8, 9, 10]) == 6
        self.assertEqual(add([6, 7, 8, 9, 10]), 6)

        # Test case 10: add([1, 3, 5, 7, 9, 11]) == 0
        self.assertEqual(add([1, 3, 5, 7, 9, 11]), 0)

if __name__ == '__main__':
    unittest.main()