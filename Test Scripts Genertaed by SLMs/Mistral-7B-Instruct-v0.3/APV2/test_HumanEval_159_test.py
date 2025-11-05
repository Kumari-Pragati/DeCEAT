You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `eat` function:


import unittest
from HumanEval_159_code import eat

class TestEatFunction(unittest.TestCase):

    def test_eat_5_6_10(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])

    def test_eat_4_8_9(self):
        self.assertEqual(eat(4, 8, 9), [12, 1])

    def test_eat_1_10_10(self):
        self.assertEqual(eat(1, 10, 10), [11, 0])

    def test_eat_2_11_5(self):
        self.assertEqual(eat(2, 11, 5), [7, 0])

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases for the `eat` function, each testing a different scenario. The test cases are written using the `unittest.TestCase` class and the `assertEqual` method to compare the expected and actual outputs. The test suite is run using the `unittest.main()` function.