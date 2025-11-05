You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_41_code import car_race_collision
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right; simultaneously, a different set of n cars
    are driving right to left. The two sets of cars start out being very far from
    each other. All cars move at the same speed. Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    return n ** 2


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_41_code import car_race_collision

class TestCarRaceCollision(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(car_race_collision(1), 1)
        self.assertEqual(car_race_collision(2), 4)
        self.assertEqual(car_race_collision(3), 9)
        self.assertEqual(car_race_collision(4), 16)
        self.assertEqual(car_race_collision(5), 25)

    def test_zero(self):
        self.assertEqual(car_race_collision(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(car_race_collision(-1), 1)
        self.assertEqual(car_race_collision(-2), 4)
        self.assertEqual(car_race_collision(-3), 9)
        self.assertEqual(car_race_collision(-4), 16)
        self.assertEqual(car_race_collision(-5), 25)

    def test_large_numbers(self):
        self.assertEqual(car_race_collision(10), 100)
        self.assertEqual(car_race_collision(20), 400)
        self.assertEqual(car_race_collision(30), 900)
        self.assertEqual(car_race_collision(40), 1600)
        self.assertEqual(car_race_collision(50), 2500)

if __name__ == '__main__':
    unittest.main()


This suite includes tests for positive numbers, zero, negative numbers, and large numbers. It checks if the function's output matches the expected result.