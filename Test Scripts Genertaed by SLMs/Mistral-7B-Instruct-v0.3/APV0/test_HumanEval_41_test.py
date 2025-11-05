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

 Here is a unittest test script for the `car_race_collision` function:


import unittest
from HumanEval_41_code import car_race_collision

class TestCarRaceCollision(unittest.TestCase):
    def test_car_race_collision(self):
        test_cases = [
            (0, 0),
            (1, 1),
            (2, 4),
            (3, 9),
            (4, 16),
            (5, 25),
            (6, 36),
            (7, 49),
            (8, 64),
            (9, 81),
            (10, 100)
        ]

        for n, expected in test_cases:
            with self.subTest(f"n={n}"):
                self.assertEqual(car_race_collision(n), expected)

if __name__ == '__main__':
    unittest.main()


This test script includes a test function `test_car_race_collision` that checks the function's output for a series of input values. The test cases are defined as a list of tuples, where each tuple contains the input value and the expected output. The `subTest` method is used to run each test case as a separate test, which can help with debugging if one test case fails.

To run the test script, save it as `test_car_race_collision.py` and execute it using the command line:


python test_car_race_collision.py


The output should show the test results, indicating whether each test case passed or failed. If all tests pass, the function is working correctly. If a test fails, you will need to investigate the issue and adjust the function or test case as necessary.