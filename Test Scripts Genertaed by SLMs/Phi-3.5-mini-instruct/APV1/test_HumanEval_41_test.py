You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_41_code import car_race_collision

class TestCarRaceCollision(unittest.TestCase):

    def test_single_car(self):
        # When there is only one car, there can be no collisions.
        self.assertEqual(car_race_collision(1), 0)

    def test_two_cars(self):
        # When there are two cars, they will collide once.
        self.assertEqual(car_race_collision(2), 4)

    def test_three_cars(self):
        # When there are three cars, each car will collide with two others.
        # However, each collision is counted twice (once for each car involved),
        # so we divide the total by 2 to get the correct number of unique collisions.
        self.assertEqual(car_race_collision(3), 3)

    def test_four_cars(self):
        # When there are four cars, each car will collide with three others.
        # Again, we divide by 2 to avoid double-counting.
        self.assertEqual(car_race_collision(4), 6)

    def test_five_cars(self):
        # When there are five cars, each car will collide with four others.
        self.assertEqual(car_race_collision(5), 10)

    def test_large_number_of_cars(self):
        # Test with a large number of cars to ensure the function scales correctly.
        # We can use a number that is a perfect square to simplify the calculation.
        self.assertEqual(car_race_collision(100), 10000)

    def test_negative_input(self):
        # Test with a negative input to ensure the function handles it appropriately.
        # Since the function specification does not mention handling negative inputs,
        # this test should fail to ensure proper error handling is implemented.
        with self.assertRaises(ValueError):
            car_race_collision(-1)

if __name__ == '__main__':
    unittest.main()