You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_159_code import eat
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    You should return a list of:
        [ total number of eaten carrots after your meals,
          the number of carrots left after your meals ]
    If there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Examples:
    eat(5, 6, 10) -> [11, 4]
    eat(4, 8, 9) -> [12, 1]
    eat(1, 10, 10) -> [11, 0]
    eat(2, 11, 5) -> [7, 0]
    """
    if need <= remaining:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_159_code import eat

class TestEat(unittest.TestCase):

    def test_enough_carrots(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])
        self.assertEqual(eat(4, 8, 9), [12, 1])
        self.assertEqual(eat(1, 10, 10), [11, 0])
        self.assertEqual(eat(2, 11, 5), [7, 0])

    def test_not_enough_carrots(self):
        self.assertEqual(eat(3, 10, 5), [8, 0])
        self.assertEqual(eat(0, 5, 5), [5, 0])
        self.assertEqual(eat(7, 15, 8), [15, 0])

if __name__ == '__main__':
    unittest.main()


This suite includes two test methods:

1. `test_enough_carrots`: This method tests the function with scenarios where there are enough remaining carrots to satisfy the need.

2. `test_not_enough_carrots`: This method tests the function with scenarios where there are not enough remaining carrots to satisfy the need.

Each test method uses the `assertEqual` method to compare the output of the `eat` function with the expected result. If the actual result matches the expected result, the test passes; otherwise, the test fails.

Please note that you need to have the `HumanEval_159_code` module with the `eat` function defined in it for these tests to work.