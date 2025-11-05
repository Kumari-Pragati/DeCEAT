user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_47_code import median
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_47_code import median

class TestMedianFunction(unittest.TestCase):

    def test_median(self):
        # Test case 1: Even number of elements
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
        
        # Test case 2: Odd number of elements
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)
        
        # Test case 3: Negative numbers
        self.assertEqual(median([-5, -3, -1, 0, 1, 3, 5]), 1)
        
        # Test case 4: Zero
        self.assertEqual(median([0, 0, 0, 0, 0]), 0)
        
        # Test case 5: Empty list
        with self.assertRaises(ValueError):
            median([])
        
        # Test case 6: Non-integer values
        self.assertEqual(median([1.5, 2.5, 3.5, 4.5]), 3.5)
        
        # Test case 7: List with duplicate values
        self.assertEqual(median([1, 2, 2, 3, 4, 5]), 3)

if __name__ == '__main__':
    unittest.main()


This test script includes seven test cases to cover different scenarios, including even and odd number of elements, negative numbers, zero, empty list, non-integer values, and list with duplicate values.