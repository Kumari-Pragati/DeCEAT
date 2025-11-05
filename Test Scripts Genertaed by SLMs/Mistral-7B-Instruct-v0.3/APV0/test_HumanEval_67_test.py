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
    return n - sum(lis)

 Here is a simple unittest test script for the `fruit_distribution` function. I've included tests for various edge cases and different fruit distributions.


import unittest
from HumanEval_67_code import fruit_distribution

class TestFruitDistribution(unittest.TestCase):

    def test_fruit_distribution(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)
        self.assertEqual(fruit_distribution("1000 apples and 1000 oranges", 2000), 0)
        self.assertEqual(fruit_distribution("1000 apples and 1 oranges", 1001), 1)
        self.assertEqual(fruit_distribution("5 apples and 6 oranges and 3 mangoes", 19), 3)
        self.assertEqual(fruit_distribution("0 apples and 1 oranges and 2 mangoes", 3), 2)
        self.assertEqual(fruit_distribution("2 apples and 3 oranges and 1 mango", 100), 96)
        self.assertEqual(fruit_distribution("100 apples and 1 oranges and 100 mangoes", 120), 20)

if __name__ == '__main__':
    unittest.main()


This script defines a test case class `TestFruitDistribution` with a single test method `test_fruit_distribution`. Inside this method, we have several test cases for different inputs and expected outputs. The `unittest.main()` call at the end runs all the tests defined in the test case class.