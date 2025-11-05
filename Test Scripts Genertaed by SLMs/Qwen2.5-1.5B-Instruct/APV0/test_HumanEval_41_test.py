system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


assistant

import unittest

# Importing the function we want to test
from HumanEval_41_code import car_race_collision

class TestCarRaceCollision(unittest.TestCase):

    def test_zero_cars(self):
        self.assertEqual(car_race_collision(0), 0)

    def test_one_car(self):
        self.assertEqual(car_race_collision(1), 1)

    def test_two_cars(self):
        self.assertEqual(car_race_collision(2), 4)

    def test_three_cars(self):
        self.assertEqual(car_race_collision(3), 9)

    def test_large_number(self):
        self.assertEqual(car_race_collision(100), 10000)

if __name__ == '__main__':
    unittest.main()


This script imports the `car_race_collision` function and defines several test cases using the `unittest.TestCase` class. Each test case checks the function against specific inputs (e.g., zero, one, two, three cars) and compares the output to the expected value. If all tests pass, it will run automatically upon execution.