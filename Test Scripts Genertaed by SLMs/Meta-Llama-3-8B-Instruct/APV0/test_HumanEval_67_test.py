user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_67_code import fruit_distribution
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit. This basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represents the total number of the fruits 
    in the basket, return the number of the mango fruits in the basket.
    
    For example:
    fruit_distribution("5 apples and 6 oranges", 19) -> 19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges", 3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges", 120) -> 120 - 100 - 1 = 19
    """
    lis = []
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)assistant

Here is the unittest test script for the `fruit_distribution` function:

import unittest
from HumanEval_67_code import fruit_distribution

class TestFruitDistribution(unittest.TestCase):
    def test_fruit_distribution(self):
        # Test cases
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)
        self.assertEqual(fruit_distribution("10 apples and 20 oranges", 50), 20)
        self.assertEqual(fruit_distribution("0 apples and 0 oranges", 10), 10)
        self.assertEqual(fruit_distribution("1 apple and 1 orange", 3), 1)
        self.assertEqual(fruit_distribution("5 apples and 5 oranges", 15), 5)
        self.assertEqual(fruit_distribution("0 apples and 0 oranges", 1), 1)

    def test_invalid_input(self):
        # Test cases with invalid input
        with self.assertRaises(ValueError):
            fruit_distribution("abc", 19)
        with self.assertRaises(ValueError):
            fruit_distribution("5 apples and 6 oranges", "not an integer")

if __name__ == '__main__':
    unittest.main()

This test script includes two test cases:

1. `test_fruit_distribution`: This test case checks the function with various input combinations to ensure it returns the correct result.
2. `test_invalid_input`: This test case checks the function with invalid input (e.g., non-integer values) to ensure it raises a `ValueError`.

You can run this script directly to execute the tests.